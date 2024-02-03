from django.urls import path
from catalog.views import index
from user.views import MusicAuthorListView

urlpatterns = [
    path('', index, name='index'),
    path("musicauthor/", MusicAuthorListView.as_view(), name='author-list'),
]


app_name = 'catalog'
