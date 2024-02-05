from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


from catalog.models import (
    MusicAuthor,
    Album,
    Genre,
    Track
)
from catalog.forms import AlbumCreationForm, AlbumUpdateForm


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
    success_url = reverse_lazy("catalog:index")
