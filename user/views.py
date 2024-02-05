from django.urls import reverse_lazy
from django.views import generic

from user.forms import MusicAuthorCreationForm, MusicAuthorUpdateForm
from user.models import MusicAuthor


# Create your views here.
class MusicAuthorListView(generic.ListView):
    model = MusicAuthor
    template_name = "catalog/music_author_list.html"
    paginate_by = 5


class MusicAuthorDetailView(generic.DetailView):
    model = MusicAuthor
    template_name = "catalog/music_author_detail.html"


class MusicAuthorCreateView(generic.CreateView):
    model = MusicAuthor
    form_class = MusicAuthorCreationForm
    template_name = "creation_forms/Author_form.html"
    success_url = reverse_lazy("user:author-list")
    queryset = MusicAuthor.objects.all().select_related("Album")


class MusicAuthorUpdateView(generic.UpdateView):
    model = MusicAuthor
    form_class = MusicAuthorUpdateForm
    template_name = "creation_forms/Author_form.html"

    def get_success_url(self):
        return reverse_lazy("user:author-detail", kwargs={"pk": self.object.pk})


class MusicAuthorDeleteView(generic.DeleteView):
    model = MusicAuthor
    template_name = "catalog/music_author_delete_confirm.html"
    success_url = reverse_lazy("catalog:index")

