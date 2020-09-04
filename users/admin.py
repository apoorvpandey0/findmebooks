from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from import_export.admin import ImportExportMixin

from import_export import resources
from import_export.admin import ExportMixin
from django.contrib.auth.admin import UserAdmin

class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','email')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

#Thsese field work like this
class ProfileAdmin(admin.ModelAdmin):
    list_display    = ('get_username','get_email','get_fullname',)
    search_fields   = ('user__username','user__email',)
    # list_editable   = (),
    # readonly_fields = (),
    # filter_horizntal= ('is_seller'),
    # list_filter     = ('is_seller'),
    # fieldsets       = (),
admin.site.register(Profile,ProfileAdmin)
