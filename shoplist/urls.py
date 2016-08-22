from django.conf.urls import url
from django.shortcuts import redirect

from shoplist.core import views

urlpatterns = (
    url(r'^$',
        views.ShoplistListView.as_view() , name="shoplist-list"),
    url(r'^delete/(?P<pk>\d+)$',
        views.ShopitemDeleteView.as_view(), name="shopitem-delete"),
    url(r'^(?P<name>[\w-]+)$',
        views.ShopitemCreateView.as_view(), name="shopitem-create"),
)
