from django.urls import path
from catalog.views import (
    index,
    AlbumListView,
    AlbumCreateView,
    AlbumDetailView,
    AlbumUpdateView,
    AlbumDeleteView,
    TrackListView,
    TrackCreateView,
    TrackDetailView,
    TrackUpdateView,
    TrackDeleteView,
    GenreListView,
    GenreCreateView,
    GenreUpdateView,
    GenreDeleteView,
    toggle_assign_to_album,
)

urlpatterns = [
    path("", index, name="index"),
    path("album/", AlbumListView.as_view(), name="album-list"),
    path("album/create/", AlbumCreateView.as_view(), name="album-create"),
    path(
        "album/<int:pk>/detail/",
        AlbumDetailView.as_view(),
        name="album-detail"
    ),
    path(
        "album/<int:pk>/update/",
        AlbumUpdateView.as_view(),
        name="album-update"
    ),
    path(
        "album/<int:pk>/delete/",
        AlbumDeleteView.as_view(),
        name="album-delete"
    ),
    path("track/", TrackListView.as_view(), name="track-list"),
    path("track/create/", TrackCreateView.as_view(), name="track-create"),
    path(
        "track/<int:pk>/detail/",
        TrackDetailView.as_view(),
        name="track-detail"
    ),
    path(
        "track/<int:pk>/update/",
        TrackUpdateView.as_view(),
        name="track-update"
    ),
    path(
        "track/<int:pk>/delete/",
        TrackDeleteView.as_view(),
        name="track-delete"
    ),
    path("genre/", GenreListView.as_view(), name="genre-list"),
    path("genre/create/", GenreCreateView.as_view(), name="genre-create"),
    path(
        "genre/<int:pk>/update/",
        GenreUpdateView.as_view(),
        name="genre-update"
    ),
    path(
        "genre/<int:pk>/delete/",
        GenreDeleteView.as_view(),
        name="genre-delete"
    ),
    path(
        "album/<int:pk>/detail/toggle-assign/",
        toggle_assign_to_album,
        name="toggle-album-assign",
    ),
]

app_name = "catalog"
