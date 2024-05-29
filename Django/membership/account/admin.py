from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

@admin.register(Account)
class CustomAccountAdmin(UserAdmin):
    list_display = ("username", "email", "phone_number", "created_at", "updated_at",)
