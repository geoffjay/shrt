"""shrt URL Configuration

'/admin' for the built-in django admin interface
'/graphql' displays the graphiql interface provided by graphene
'/<str:tag>' redirects to the URL that matches the shorted tag
"""

from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView

from shrt.url.views import UrlView

def favicon(request):
    """Provides a transparent 16x16 favicon to suppress django errors"""
    from textwrap import dedent
    from django.http import HttpResponse
    import base64

    icon = """\
    AAABAAEAEBACAAEAAQCwAAAAFgAAACgAAAAQAAAAIAAAAAEAAQAAAAAAgAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAA////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD/
    /wAA//8AAP//AAD//wAA//8AAP//AAD//wAA"""
    icon = dedent(icon)
    icon = base64.b64decode(icon)

    return HttpResponse(icon, content_type="image/x-icon")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql', GraphQLView.as_view(graphiql=True)),
    path('favicon.ico', favicon, name='favicon'),
    path('<str:tag>', UrlView.as_view()),
]
