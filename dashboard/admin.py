from django.contrib import admin
from . import dash_mod

# Register your models here.
admin.site.register(dash_mod.Operator)
admin.site.register(dash_mod.Role)