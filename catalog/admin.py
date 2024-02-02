from django.contrib import admin

from catalog.models import Album, Genre, Track


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("release_date",)


admin.site.register(Genre)
admin.site.register(Track)
