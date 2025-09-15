from bot.models import Staff
from unfold.admin import ModelAdmin
from django.contrib import admin

@admin.register(Staff)
class StaffAdmin(ModelAdmin):
    list_display = ["user_id", "name"]