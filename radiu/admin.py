from django.contrib import admin
from radiu.models import Artist, Song, UserProfile, Comment, Like

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'genre')
    prepopulated_fields = {'slug': ('title',)}

class ArtistAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'song')

class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'song')

# Register your models here.
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(UserProfile)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)