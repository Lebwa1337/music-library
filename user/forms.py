from django.contrib.auth.forms import UserCreationForm
from django import forms

from user.models import MusicAuthor


class MusicAuthorCreationForm(UserCreationForm):
    creation_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    band_members = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
    record_label = forms.CharField(widget=forms.Textarea(attrs={"rows": 1}))

    class Meta(UserCreationForm.Meta):
        model = MusicAuthor
        fields = UserCreationForm.Meta.fields + (
            "creation_date",
            "band_members",
            "record_label",
        )
