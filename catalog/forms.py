from django import forms
from django.contrib.auth import get_user_model

from catalog.models import Album, Track, Genre
from user.models import MusicAuthor


class AlbumCreationForm(forms.ModelForm):
    # author = forms.ModelMultipleChoiceField(
    #     queryset=get_user_model().objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    # )
    release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 4}))

    class Meta:
        model = Album
        fields = [
            "name",
            "description",
            "release_date",
            "author"
        ]


class AlbumUpdateForm(forms.ModelForm):
    # author = forms.ModelMultipleChoiceField(
    #         queryset=get_user_model().objects.all(),
    #         widget=forms.CheckboxSelectMultiple,
    #     )
    release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 4}))
    tracks = forms.ModelMultipleChoiceField(
        queryset=Track.objects.all(),
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Album
        fields = [
            "name",
            "description",
            "release_date",
            "author",
            "tracks"
        ]


# class SingleCheckboxInput(forms.CheckboxInput):
#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     self.input_type = 'radio'
#     #     self.attrs['type'] = 'radio'


class TrackForm(forms.ModelForm):
    # author = forms.ModelChoiceField(
    #         queryset=get_user_model().objects.all,
    #         widget=forms.ChoiceField,
    #     )
    duration = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}), input_formats=["%M:%S"])
    release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["author"].queryset = get_user_model().objects.all()

    class Meta:
        model = Track
        fields = ['name', 'duration', 'author', 'genre', 'lyrics']


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ["name", ]
