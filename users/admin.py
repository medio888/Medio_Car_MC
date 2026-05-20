from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone', 'region')
    search_fields = ('email', 'first_name', 'last_name', 'phone')
    list_filter = ('region',)