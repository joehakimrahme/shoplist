from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


from shoplist.core.models import Shoplist
from shoplist.core.models import Shopitem
from shoplist.core.forms import ShopitemForm


JB_SHOPLIST = "Shopping"


@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == "GET":
        return HttpResponseRedirect(
            reverse("shoplist.core.views.shoplist", args=[JB_SHOPLIST]))


@require_http_methods(["DELETE"])
def item(request, shoplist_name, item_id):
    if request.method == "DELETE":
        item = Shopitem.objects.get(id=item_id)
        item.delete()

        return HttpResponse()


@require_http_methods(["GET", "POST", "DELETE"])
def shoplist(request, shoplist_name):
    if request.method == "GET":
        shoplist, created = Shoplist.objects.get_or_create(name=shoplist_name)
        form = ShopitemForm()

        return render(request, 'index.html', {'shoplist': shoplist,
                                              'form': form})
    elif request.method == "POST":
        form = ShopitemForm(request.POST)
        shoplist = get_object_or_404(Shoplist, name=shoplist_name)
        if form.is_valid():
            item = Shopitem(name=form.cleaned_data["name"])
            shoplist.shopitem_set.add(item)

        return HttpResponseRedirect(
            reverse("shoplist.core.views.shoplist", args=[shoplist_name]))
