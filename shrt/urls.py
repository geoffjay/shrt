"""shrt URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from graphene_django.views import GraphQLView

from shrt.url.views import UrlView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql', GraphQLView.as_view(graphiql=True)),
    path('<str:tag>', UrlView.as_view()),
]
