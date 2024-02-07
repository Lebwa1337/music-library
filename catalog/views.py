from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


from catalog.models import (
    MusicAuthor,
    Album,
    Genre,
    Track
)
from catalog.forms import AlbumCreationForm, AlbumUpdateForm, TrackForm, GenreForm


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


class AlbumListView(generic.ListView):
    model = Album
    template_name = "catalog/album_list.html"
    paginate_by = 5
    queryset = Album.objects.all().select_related("tracks")


class AlbumCreateView(generic.CreateView):
    model = Album
    template_name = "creation_forms/album_form.html"
    form_class = AlbumCreationForm
    success_url = reverse_lazy("catalog:album-list")


class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = "catalog/album_detail.html"


class AlbumUpdateView(generic.UpdateView):
    model = Album
    template_name = "creation_forms/album_form.html"
    form_class = AlbumUpdateForm

    def get_success_url(self):
        return reverse_lazy("catalog:album-detail", kwargs={"pk": self.object.pk})


class AlbumDeleteView(generic.DeleteView):
    model = Album
    template_name = "catalog/album_delete_confirm.html"
    success_url = reverse_lazy("catalog:album-list")


def toggle_assign_to_album(request, pk):
    author = MusicAuthor.objects.get(id=request.user.id)
    if Album.objects.get(id=pk) in author.album_set.all():
        author.album_set.remove(Album.objects.get(id=pk))
    else:
        author.album_set.add(Album.objects.get(id=pk))
    return HttpResponseRedirect(reverse_lazy("catalog:album-detail", args=[pk]))


class TrackListView(generic.ListView):
    model = Track
    template_name = "catalog/track_list.html"
    paginate_by = 5
    queryset = Track.objects.all().prefetch_related("genre")


class TrackCreateView(generic.CreateView):
    model = Track
    form_class = TrackForm
    template_name = "creation_forms/track_form.html"
    success_url = reverse_lazy("catalog:track-list")


class TrackDetailView(generic.DetailView):
    model = Track
    template_name = "catalog/track_detail.html"


class TrackUpdateView(generic.UpdateView):
    model = Track
    form_class = TrackForm
    template_name = "creation_forms/track_form.html"

    def get_success_url(self):
        return reverse_lazy("catalog:track-detail", kwargs={"pk": self.object.pk})


class TrackDeleteView(generic.DeleteView):
    model = Track
    template_name = "catalog/track_delete_confirm.html"
    success_url = reverse_lazy("catalog:track-list")


class GenreListView(generic.ListView):
    model = Genre
    template_name = "catalog/genre_list.html"
    paginate_by = 5


class GenreCreateView(generic.CreateView):
    model = Genre
    form_class = GenreForm
    template_name = "creation_forms/genre_form.html"
    success_url = reverse_lazy("catalog:genre-list")


class GenreUpdateView(generic.UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = "creation_forms/genre_form.html"

    def get_success_url(self):
        return reverse_lazy("catalog:genre-detail", kwargs={"pk": self.object.pk})


class GenreDeleteView(generic.DeleteView):
    model = Genre
    template_name = "catalog/genre_delete_confirm.html"
    success_url = reverse_lazy("catalog:genre-list")
