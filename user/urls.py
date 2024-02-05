from django.urls import path

from user.views import MusicAuthorCreateView, MusicAuthorDetailView, MusicAuthorUpdateView, MusicAuthorDeleteView

urlpatterns = [
    path("musicauthor/create/", MusicAuthorCreateView.as_view(), name='author-create'),
    path("musicauthor/<int:pk>/detail/", MusicAuthorDetailView.as_view(), name='author-detail'),
    path("musicauthor/<int:pk>/update/", MusicAuthorUpdateView.as_view(), name='author-update'),
    path("musicauthor/<int:pk>/delete/", MusicAuthorDeleteView.as_view(), name='author-delete')

]

app_name = 'user'
