from django.conf.urls import patterns
from django.conf.urls import url

from shoplist.core import views


urlpatterns = patterns(
    '',
    # TODO(rahmu): this should point to a "new shoplist" form
    url(r'^$', views.index, name="index"),
    url(r'^(?P<shoplist_name>[\w ]+)$', views.shoplist, name="shoplist"),
    url(r'^(?P<shoplist_name>[\w ]+)/(?P<item_id>\d+)$', views.item, name="item"),
)
