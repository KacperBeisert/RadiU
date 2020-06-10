from django.conf.urls import url
from radiu import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^myprofile/(?P<user_name_slug>[\w\-]+)/$', views.myprofile, name='myprofile'),
    url(r'^submit_song/$', views.submit_song, name='submit_song'),
    url(r'^add_artist/$', views.add_artist, name='add_artist'),
    url(r'^artist/(?P<artist_name_slug>[\w\-]+)/$', views.artist, name='artist'),
    url(r'^song/(?P<song_title_slug>[\w\-]+)/$', views.song, name='song'),
    url(r'^like/$', views.like_unlike, name='like_unlike'),
    url(r'^search/$', views.search, name='search'),
    url(r'^favourite/$', views.fav_unfav, name='fav_unfav'),
    url(r'^myprofile/(?P<user_name_slug>[\w\-]+)/update_picture/$', views.myprofile, name='update_picture'),
    url(r'^song/(?P<song_title_slug>[\w\-]+)/submit_comment/$', views.submit_comment, name='submit_comment'),
    url(r'^delete_song/$', views.delete_song, name='delete_song'),
    url(r'^delete_artist/$', views.delete_artist, name='delete_artist'),
]
