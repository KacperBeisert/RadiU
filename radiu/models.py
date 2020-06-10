from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000, blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Song(models.Model):
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=100, unique=True)
    genre = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Song, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    register_date = models.DateField(auto_now_add=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    favourite_song = models.ForeignKey(Song, blank=True, null=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    user = models.ForeignKey(User)
    song = models.ForeignKey(Song)
    datetime = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.user.username

class Like(models.Model):
    user = models.ForeignKey(User)
    song = models.ForeignKey(Song)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username, self.song.title
