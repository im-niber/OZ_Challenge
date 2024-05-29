from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("testcol", "username", "email", "first_name", "last_name", "is_staff", "is_business", "grade")
    # fieldsets = (
    #     (None, {"fields": ("username", "password", "is_business")}),
    # )