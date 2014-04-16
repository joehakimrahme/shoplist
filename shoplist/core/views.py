from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


from shoplist.core.models import Shoplist
from shoplist.core.models import Shopitem
from shoplist.core.forms import ShopitemForm


JB_SHOPLIST = "Joe and Bia's shopping list"


@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == "GET":

        sl, created = Shoplist.objects.get_or_create(name=JB_SHOPLIST)
        form = ShopitemForm()

        return render(request, 'index.html', {'shoplist': sl,
                                              'form': form})

    elif request.method == "POST":
        sl, created = Shoplist.objects.get_or_create(name=JB_SHOPLIST)

        form = ShopitemForm(request.POST)

        if form.is_valid():
            item = Shopitem(name=form.cleaned_data["name"])
            sl.shopitem_set.add(item)

        return HttpResponseRedirect(reverse("shoplist.core.views.index"))


@require_http_methods(["DELETE"])
def item(request, item_id):
    if request.method == "DELETE":
        item = Shopitem.objects.get(id=item_id)
        item.delete()

        return HttpResponseRedirect(reverse("shoplist.core.views.index"))
