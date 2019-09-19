from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect

from shrt.url.models import Url

class UrlView(View):
    """Redirect view.

    Handles a shortened URL by using the redirect shortcut.
    """

    def get(self, request, tag):
        # url = Url.objects.get(tag=tag)
        url = Url.objects.get(shortened=tag)
        response = redirect(url.original)
        return response
