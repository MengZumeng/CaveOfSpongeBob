from django.contrib import admin
from .models import Myuser


@admin.register(Myuser)
class OuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')
    fieldsets = (
        ('个人信息', {'fields': (('username', 'nickname'), 'email','avatar')}),
        ('权限信息', {'fields': (('is_active', 'is_staff', 'is_superuser'),
                             'groups', 'user_permissions')}),
        ('重要日期', {'fields': (('last_login', 'date_joined'),)}),
    )
    filter_horizontal = ('groups', 'user_permissions',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'nickname', 'email')