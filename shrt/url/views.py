from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect

from shrt.url.models import Url

class UrlView(View):
    def get(self, request, tag):
        url = Url.objects.get(pk=5)
        response = redirect(url.name)
        return response
