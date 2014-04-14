from django.conf.urls import patterns
from django.conf.urls import url

from shoplist.core import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index),
    url(r'new_item', views.add_item, name="new_item"),
    url(r'remove/(?P<item_id>\d+)', views.remove_item, name="remove_item"),
)
