from django.conf.urls import patterns
from django.conf.urls import url

from shoplist.core import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name="index"),
    url(r'(?P<item_id>\d+)', views.item, name="item"),
)
