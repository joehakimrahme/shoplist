from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


from shoplist.core.models import Shoplist
from shoplist.core.models import Shopitem


JB_SHOPLIST = "Joe and Bia's shopping list"


@require_http_methods(["GET"])
def index(request):
    sl, created = Shoplist.objects.get_or_create(name=JB_SHOPLIST)

    return render(request, 'index.html', {'shoplist': sl})


@require_http_methods(["POST"])
def add_item(request):
    sl, created = Shoplist.objects.get_or_create(name=JB_SHOPLIST)
    item = Shopitem(name=request.POST['newitem'])
    sl.shopitem_set.add(item)

    return HttpResponseRedirect(reverse("shoplist.core.views.index"))


@require_http_methods(["DELETE"])
def remove_item(request, item_id):
    item = Shopitem.objects.get(id=item_id)
    item.delete()

    return HttpResponseRedirect(reverse("shoplist.core.views.index"))
