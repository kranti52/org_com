from django.conf.urls import url
from rest_framework import routers

from .views import InformationalSystemView
from .views import MapView

router = routers.DefaultRouter()

urlpatterns = [
    url(r'(?P<id>[\d]+)/(?P<entity_type>["product"|"issue"|"metric"]+)$', InformationalSystemView.as_view(),
        name='entity-update-delete'),
    url(r'(?P<entity_type>["product"|"issue"|"metric"]+)$', InformationalSystemView.as_view(),
        name='entity-create-fetch'),
    url(r'map/$', MapView.as_view(), name='entity-map'),
]
