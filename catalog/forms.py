from django import forms

from catalog.models import Album, Track, Genre


class AlbumCreationForm(forms.ModelForm):
    release_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 4}))

    class Meta:
        model = Album
        fields = ["name", "description", "release_date", "author"]


class AlbumUpdateForm(forms.ModelForm):
    release_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 4}))

    class Meta:
        model = Album
        fields = [
            "name",
            "description",
            "release_date",
            "author",
        ]


class TrackForm(forms.ModelForm):
    release_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    duration = forms.DurationField(
        widget=forms.TextInput(
            attrs={"placeholder": "Write duration in SECONDS"}
        )
    )

    class Meta:
        model = Track
        fields = ["name", "duration", "author", "genre", "lyrics", "album"]


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = [
            "name",
        ]


class AlbumSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by album name"}),
    )


class TrackSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by track name"}),
    )


class GenreSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by genre name"}),
    )
