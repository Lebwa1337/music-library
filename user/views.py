from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from user.forms import MusicAuthorCreationForm, MusicAuthorUpdateForm, MusicAuthorSearchForm
from user.models import MusicAuthor


# Create your views here.
class MusicAuthorListView(LoginRequiredMixin, generic.ListView):
    model = MusicAuthor
    template_name = "catalog/music_author_list.html"
    paginate_by = 5
    queryset = MusicAuthor.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MusicAuthorListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username")
        context["search_form"] = MusicAuthorSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        form = MusicAuthorSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return self.queryset


class MusicAuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = MusicAuthor
    template_name = "catalog/music_author_detail.html"


class MusicAuthorCreateView(LoginRequiredMixin, generic.CreateView):
    model = MusicAuthor
    form_class = MusicAuthorCreationForm
    template_name = "creation_forms/Author_form.html"
    success_url = reverse_lazy("user:author-list")
    queryset = MusicAuthor.objects.all().select_related("Album")


class MusicAuthorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = MusicAuthor
    form_class = MusicAuthorUpdateForm
    template_name = "creation_forms/Author_form.html"

    def get_success_url(self):
        return reverse_lazy("user:author-detail", kwargs={"pk": self.object.pk})


class MusicAuthorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = MusicAuthor
    template_name = "catalog/music_author_delete_confirm.html"
    success_url = reverse_lazy("catalog:index")

