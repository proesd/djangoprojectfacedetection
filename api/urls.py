from rest_framework import routers
from .views import BukuTamuViews
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from api import views as app_views
schema_view = get_swagger_view(title='Pastebin API')

router = routers.SimpleRouter()
router.register(r'bukutamu', BukuTamuViews)
urlpatterns = [
    url(r'^',app_views.index),
    url(r'^docs', schema_view)
]
urlpatterns += router.urls