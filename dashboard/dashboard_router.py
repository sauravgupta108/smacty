from django.urls import include, path
from . import dashboard_views as dview
from . import auth_views 

app_name = 'dashboard'
urlpatterns = [
    path('', dview.misc_views.index, name = 'home'),
    path('login', auth_views.auth_login, name = 'dashLogin' ),
    path('logout', auth_views.auth_logout, name = 'dashLogout'),
    path('contact', dview.misc_views.contact, name = 'contact'),
    path('about', dview.misc_views.about, name = 'about'),
    path('lights', dview.light_views.all_lights, name='all_lights'),
    path('dustbins', dview.dustbin_views.all_dustbins, name='all_dustbins'),
    path('tanks', dview.tank_views.all_water_tanks, name='all_water_tanks'),
    # path('publish', dview.misc_views.publish, name = 'publish'),
    # path('subscribe', dview.misc_views.subscribe, name = 'subscribe'),
]