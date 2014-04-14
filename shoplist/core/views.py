from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render


from shoplist.core.models import Shoplist
from shoplist.core.models import Shopitem


JB_SHOPLIST = "Joe and Bia's shopping list"


def index(request):
    sl = Shoplist.objects.get_or_create(name=JB_SHOPLIST)[0]

    return render(request, 'index.html', {'shoplist': sl})


def add_item(request):
    sl = Shoplist.objects.get_or_create(name=JB_SHOPLIST)[0]
    item = Shopitem(name=request.POST['newitem'])
    sl.shopitem_set.add(item)

    return HttpResponseRedirect(reverse("shoplist.core.views.index"))


def remove_item(request, item_id):
    item = Shopitem.objects.get(id=item_id)
    item.delete()

    return HttpResponseRedirect(reverse("shoplist.core.views.index"))
