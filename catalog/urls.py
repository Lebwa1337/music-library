from django.urls import path
from catalog.views import (
    index,
    AlbumListView,
    AlbumCreateView,
    AlbumDetailView,
    AlbumUpdateView,
    AlbumDeleteView
)

urlpatterns = [
    path('', index, name='index'),
    path("album/", AlbumListView.as_view(), name='album-list'),
    path("album/create/", AlbumCreateView.as_view(), name='album-create'),
    path("album/<int:pk>/detail", AlbumDetailView.as_view(), name='album-detail'),
    path("album/<int:pk>/update/", AlbumUpdateView.as_view(), name='album-update'),
    path("album/<int:pk>/delete/", AlbumDeleteView.as_view(), name='album-delete')
]


app_name = 'catalog'
