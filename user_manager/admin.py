from django.contrib import admin
from .models import OwnUser


class OwnUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'address', 'create_time')
    search_fields = ('name',)


admin.site.register(OwnUser, OwnUserAdmin)
