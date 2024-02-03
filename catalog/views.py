from django.shortcuts import render
from django.views import generic


from catalog.models import (
    MusicAuthor,
    Album,
    Genre,
    Track
)


def index(request):

    num_authors = MusicAuthor.objects.count()
    num_albums = Album.objects.count()
    num_genres = Genre.objects.count()
    num_tracks = Track.objects.count()

    context = {
        "num_authors": num_authors,
        "num_albums": num_albums,
        "num_genres": num_genres,
        "num_tracks": num_tracks,
    }

    return render(request, "catalog/index.html", context=context)



