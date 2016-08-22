import json

from django.http import HttpResponse
from django.views import generic

from shoplist.core import models


class ShoplistListView(generic.ListView):
    model = models.Shoplist
    template_name = 'shoplist-list.html'


class ShopitemCreateView(generic.CreateView):
    model = models.Shopitem
    fields = ['name']
    template_name = 'shopitem-create.html'

    def get_context_data(self, **kwargs):
        context = super(ShopitemCreateView, self).get_context_data(**kwargs)
        try:
            context['shoplist'] = models.Shoplist.objects.get(
                name=self.kwargs['name'])
        except models.Shoplist.DoesNotExist:
            pass
        context['list_name'] = self.kwargs['name']
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        shoplist, _ = models.Shoplist.objects.get_or_create(
            name=self.kwargs['name'])

        instance.shoplist = shoplist
        instance.save()
        return super(ShopitemCreateView, self).form_valid(form)


class ShopitemDeleteView(generic.DeleteView):
    model = models.Shopitem

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        payload = {'delete': 'ok'}
        return HttpResponse(json.dumps(payload),
                            content_type='application/json')
