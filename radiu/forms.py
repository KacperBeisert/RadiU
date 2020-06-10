from django import forms
from radiu.models import Song, UserProfile, Artist, Comment
from django.contrib.auth.models import User

class ArtistForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1000, required=False)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Artist
        exclude = ('slug',)

class SongForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    genre = forms.CharField(max_length=50)
    url = forms.URLField(max_length=200)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    artists = Artist.objects.all().order_by('-id')
    artist = forms.ModelChoiceField(queryset=artists)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('https://'):
            url = 'https://' + url
            cleaned_data['url'] = url
        return cleaned_data

    class Meta:
        model = Song
        exclude = ('slug',)

class CommentForm(forms.ModelForm):
    text = forms.CharField(max_length=250)

    class Meta:
        model = Comment
        fields = ('text',)

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=20)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    favourite_song = forms.CharField(max_length=100, required=False)
    slug = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        favourite_song_id = cleaned_data.get('favourite_song')
        if favourite_song_id:
            song = Song.objects.get(id=favourite_song_id)
            cleaned_data['favourite_song'] = song
        else:
            cleaned_data['favourite_song'] = None
        return cleaned_data

    class Meta:
        model = UserProfile
        fields = ('favourite_song', 'picture')

class UpdatePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
