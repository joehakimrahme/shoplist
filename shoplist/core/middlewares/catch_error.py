from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseRedirect


class HttpResponseNotAllowedMiddleware(object):
    def process_response(self, request, response):
        if isinstance(response, HttpResponseNotAllowed):
            messages.add_message(
                request,
                messages.ERROR,
                "The method {} is not allowed on this resource".format(
                    request.method))

            return HttpResponseRedirect(reverse("shoplist.core.views.index"))

        return response
