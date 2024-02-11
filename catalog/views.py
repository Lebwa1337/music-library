from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


from catalog.models import MusicAuthor, Album, Genre, Track
from catalog.forms import (
    AlbumCreationForm,
    AlbumUpdateForm,
    TrackForm,
    GenreForm,
    AlbumSearchForm,
    TrackSearchForm,
    GenreSearchForm,
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


class AlbumListView(LoginRequiredMixin, generic.ListView):
    model = Album
    template_name = "catalog/album_list.html"
    paginate_by = 5
    queryset = Album.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AlbumListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name")
        context["search_form"] = AlbumSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        form = AlbumSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return self.queryset


class AlbumCreateView(LoginRequiredMixin, generic.CreateView):
    model = Album
    template_name = "creation_forms/album_form.html"
    form_class = AlbumCreationForm
    success_url = reverse_lazy("catalog:album-list")


class AlbumDetailView(LoginRequiredMixin, generic.DetailView):
    model = Album
    template_name = "catalog/album_detail.html"


class AlbumUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Album
    template_name = "creation_forms/album_form.html"
    form_class = AlbumUpdateForm

    def get_success_url(self):
        return reverse_lazy(
            "catalog:album-detail",
            kwargs={"pk": self.object.pk}
        )


class AlbumDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Album
    template_name = "catalog/album_delete_confirm.html"
    success_url = reverse_lazy("catalog:album-list")


def toggle_assign_to_album(request, pk):
    author = MusicAuthor.objects.get(id=request.user.id)
    if Album.objects.get(id=pk) in author.albums.all():
        author.albums.remove(Album.objects.get(id=pk))
    else:
        author.albums.add(Album.objects.get(id=pk))
    return HttpResponseRedirect(
        reverse_lazy("catalog:album-detail", args=[pk])
    )


class TrackListView(LoginRequiredMixin, generic.ListView):
    model = Track
    template_name = "catalog/track_list.html"
    paginate_by = 5
    queryset = Track.objects.all().prefetch_related("genre")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TrackListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name")
        context["search_form"] = TrackSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        form = TrackSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return self.queryset


class TrackCreateView(LoginRequiredMixin, generic.CreateView):
    model = Track
    form_class = TrackForm
    template_name = "creation_forms/track_form.html"
    success_url = reverse_lazy("catalog:track-list")
    queryset = Track.objects.all().select_related("track")


class TrackDetailView(LoginRequiredMixin, generic.DetailView):
    model = Track
    template_name = "catalog/track_detail.html"


class TrackUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Track
    form_class = TrackForm
    template_name = "creation_forms/track_form.html"

    def get_success_url(self):
        return reverse_lazy(
            "catalog:track-detail", kwargs={"pk": self.object.pk}
        )


class TrackDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Track
    template_name = "catalog/track_delete_confirm.html"
    success_url = reverse_lazy("catalog:track-list")


class GenreListView(LoginRequiredMixin, generic.ListView):
    model = Genre
    template_name = "catalog/genre_list.html"
    paginate_by = 5
    queryset = Genre.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GenreListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name")
        context["search_form"] = GenreSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        form = GenreSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return self.queryset


class GenreCreateView(LoginRequiredMixin, generic.CreateView):
    model = Genre
    form_class = GenreForm
    template_name = "creation_forms/genre_form.html"
    success_url = reverse_lazy("catalog:genre-list")


class GenreUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = "creation_forms/genre_form.html"

    def get_success_url(self):
        return reverse_lazy(
            "catalog:genre-detail", kwargs={"pk": self.object.pk}
        )


class GenreDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Genre
    template_name = "catalog/genre_delete_confirm.html"
    success_url = reverse_lazy("catalog:genre-list")
