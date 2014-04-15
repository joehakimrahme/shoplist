from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


from shoplist.core.models import Shoplist
from shoplist.core.models import Shopitem
from shoplist.core.forms import ShopitemForm


JB_SHOPLIST = "Joe and Bia's shopping list"


@require_http_methods(["GET"])
def index(request):
    sl, created = Shoplist.objects.get_or_create(name=JB_SHOPLIST)

    form = ShopitemForm()

    return render(request, 'index.html', {'shoplist': sl,
                                          'form': form})


@require_http_methods(["POST"])
def add_item(request):
    sl, created = Shoplist.objects.get_or_create(name=JB_SHOPLIST)

    form = ShopitemForm(request.POST)

    if form.is_valid():
        item = Shopitem(name=form.cleaned_data["name"])
        sl.shopitem_set.add(item)

    return HttpResponseRedirect(reverse("shoplist.core.views.index"))


@require_http_methods(["DELETE"])
def remove_item(request, item_id):
    item = Shopitem.objects.get(id=item_id)
    item.delete()

    return HttpResponseRedirect(reverse("shoplist.core.views.index"))
