from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import MusicAuthor


@admin.register(MusicAuthor)
class MusicAuthorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("creation_date",)
    fieldsets = UserAdmin.fieldsets + (
        (('Personal info', {"fields": ('creation_date',)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "band_members",
                        "record_label",
                        "creation_date",
                    )
                },
            ),
        )
    )