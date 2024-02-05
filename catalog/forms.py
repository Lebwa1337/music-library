from django import forms
from django.contrib.auth import get_user_model

from catalog.models import Album


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

    class Meta:
        model = Album
        fields = [
            "name",
            "description",
            "release_date",
            "author"
        ]
