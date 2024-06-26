from django.contrib import admin

from users.models import User
from habit.models import Habit

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "phone",
    )
    list_filter = ("email",)
    search_fields = (
        "email",
    )

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "action",
        "user",
        "is_published",
    )
    list_filter = ("user",)
    search_fields = (
        "action",
    )
