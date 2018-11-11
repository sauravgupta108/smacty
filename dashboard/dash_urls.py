from django.urls import include, path
from . import dash_views as dv

urlpatterns = [
    path('', dv.index, name = 'index'),
    path('publish', dv.publish, name = 'publish'),
    path('subscribe', dv.subscribe, name = 'subscribe'),
]