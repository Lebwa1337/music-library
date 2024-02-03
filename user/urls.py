from django.urls import path

from user.views import MusicAuthorCreateView, MusicAuthorDetailView

urlpatterns = [
    path("musicauthor/create/", MusicAuthorCreateView.as_view(), name='author-create'),
    path("musicauthor/<int:pk>/detail/", MusicAuthorDetailView.as_view(), name='author-detail'),

]


app_name = 'user'
