from rest_framework import routers
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from api import views as app_views
schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^create_dataset',app_views.create_dataset),
    url(r'^details/(?P<id>[0-9]+)$', app_views.details, name='details'),
    url(r'^detect',app_views.detect),
    url(r'^train',app_views.trainer),
    url(r'^docs', schema_view)
]