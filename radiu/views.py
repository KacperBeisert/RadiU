from django.shortcuts import render
from radiu.forms import UserForm, UserProfileForm, UpdatePictureForm
from radiu.forms import SongForm, ArtistForm, CommentForm
from radiu.models import Song, Artist, Comment, Like, UserProfile
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout

def home(request):
    likes = {}
    songs = Song.objects.all()
    for i in range(len(songs) - 1):
        likes[songs[i].title] = Like.objects.filter(song=songs[i]).count()
    most_liked_songs = []
    for i in range(10):
        title = max(likes, key=likes.get)
        most_liked_song = Song.objects.filter(title=title)[0]
        most_liked_songs.append({'rank': i+1, 'song': most_liked_song, 'likes': likes[title]})
        del likes[title]
    most_liked_song = most_liked_songs[0]['song']
    video_id = most_liked_song.url[32:]
    context_dict = {"songlist": most_liked_songs, "video_id": video_id}
    liked = get_liked_songs(request, most_liked_songs)
    if liked:
        context_dict['liked'] = liked
    return render(request, 'radiu/home.html', context=context_dict)

# Helper function used to verify which songs were already liked by the user.
def get_liked_songs(request, song_list):
    song_list_song_ids = []
    for item in song_list:
        song_list_song_ids.append(item['song'].id)
    if request.user.is_authenticated():
        user_likes = Like.objects.filter(user=request.user)
        user_likes_song_ids = []
        for item in user_likes:
            user_likes_song_ids.append(item.song.id)
        liked_songs = []
        for song_id in song_list_song_ids:
            if song_id in user_likes_song_ids:
                liked_songs.append(song_id)
        return liked_songs
    else:
        return False

def song(request, song_title_slug):
    context_dict = {}
    try:
        song = Song.objects.get(slug=song_title_slug)
        comments = Comment.objects.filter(song=song)
        context_dict['song'] = song
        context_dict['comments'] = comments
        if request.user.is_authenticated():
            try:
                user_favourite_song_id = UserProfile.objects.get(user=request.user).favourite_song.id
            except:
                user_favourite_song_id = None
            if user_favourite_song_id == song.id:
                context_dict['is_favourite'] = True
        else:
            context_dict['is_favourite'] = False
        liked = get_liked_songs(request, [{'song': song}])
        if liked:
            context_dict['liked'] = liked
        video_id = song.url[32:]
        context_dict['video_id'] = video_id
        likes = Like.objects.filter(song=song).count()
        context_dict['likes'] = likes
        faves = UserProfile.objects.filter(favourite_song=song).count()
        context_dict['faves'] = faves
    except Song.DoesNotExist:
        context_dict['song'] = None
        context_dict['comments'] = None
    return render(request, 'radiu/song.html', context=context_dict)

@login_required
def like_unlike(request):
    song_id = None
    user_id = request.user.id
    if request.method == 'GET':
        song_id = int(request.GET['song_id'])
        addsub = request.GET['addsub']
        action = 'failed'
        if song_id and user_id:
            if addsub == 'no':
                new_like = Like(user_id=user_id, song_id=song_id)
                new_like.save()
                action = 'add'
            elif addsub == 'yes':
                Like.objects.get(user_id=user_id, song_id=song_id).delete()
                action = 'sub'
    return HttpResponse(action)

@login_required
def fav_unfav(request):
    if request.method == 'GET':
        profile = UserProfile.objects.get(user=request.user)
        fav_unfav = request.GET['favunfav']
        song_id = request.GET['song_id']
        if fav_unfav == 'yes':
            profile.favourite_song_id = None
            action = 'removed'
        elif fav_unfav == 'no':
            profile.favourite_song_id = song_id
            action = 'set'
        profile.save()
    return HttpResponse(action)

def artist(request, artist_name_slug):
    context_dict = {}
    try:
        artist = Artist.objects.get(slug=artist_name_slug)
        songs = Song.objects.filter(artist=artist)
        context_dict['artist'] = artist
        context_dict['songs'] = songs
        likes = {}
        for i in range(len(songs)):
            likes[songs[i].title] = Like.objects.filter(song=songs[i]).count()
        title = max(likes, key=likes.get)
        most_liked_song = Song.objects.get(title=title)
        video_id = most_liked_song.url[32:]
        context_dict["most_liked_song"] = most_liked_song
        context_dict["video_id"] = video_id
    except Artist.DoesNotExist:
        context_dict['artist'] = None
        context_dict['songs'] = None
    return render(request, 'radiu/artist.html', context=context_dict)

def about(request):
    context_dict = {}
    return render(request, 'radiu/about.html', context=context_dict)

@login_required
def submit_comment(request, song_title_slug):
    song = Song.objects.get(slug=song_title_slug)
    context_dict = {}
    commented = False
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = user
                comment.song = song
                comment.save()
                commented = True
            else:
                context_dict = {'comment_error': comment_form.errors}
                return render(request, 'radiu/submit_comment.html', context_dict)
        else:
            comment_form = CommentForm()
    context_dict = {'comment_form': comment_form, 'commented': commented, 'song': song}
    return render(request, 'radiu/submit_comment.html', context_dict)

@login_required
def myprofile(request, user_name_slug):
    context_dict = {}
    if request.user.is_authenticated():
        user = request.user
        profile = UserProfile.objects.get(user=user)
        context_dict['profile'] = profile
        context_dict['user'] = user
        fav_song = profile.favourite_song
        if fav_song:
            context_dict['video_id'] = fav_song.url[32:]
        else:
            fav_song = False
        context_dict['fav_song'] = fav_song
        # Get all user's liked songs in order.
        user_likes = Like.objects.filter(user=user).order_by('-datetime')
        liked_songs = []
        genre_dict = {}
        if user_likes:
            for like in user_likes:
                song = Song.objects.get(id=like.song.id)
                liked_songs.append(song)
                genre = song.genre
                if genre in genre_dict:
                    genre_dict[genre] += 1
                else:
                    genre_dict[genre] = 1
            num_likes = len(liked_songs)
            # Build list: [genre, number of likes]
            liked_genres = []
            while len(genre_dict) > 0:
                most_liked_genre = max(genre_dict, key=genre_dict.get)
                liked_genres.append([most_liked_genre, genre_dict[most_liked_genre]])
                del genre_dict[most_liked_genre]
            fav_genre = liked_genres[0][0]
            suggested_songs= get_suggestions(request, fav_genre)
        else:
            liked_songs = False
            num_likes = 0
            liked_genres = False
            suggested_songs = False
        if liked_songs:
            liked_songs = liked_songs[:10]
        context_dict['liked_songs'] = liked_songs
        context_dict['likes'] = num_likes
        context_dict['liked_genres'] = liked_genres
        context_dict['suggested_songs'] = suggested_songs
        # Count number of user's comments.
        all_comments = Comment.objects.filter(user=user)
        if all_comments:
            comments = len(all_comments)
        else:
            comments = 0
        context_dict['comments'] = comments
        user_profile = UserProfile.objects.get(user=request.user)
        updated = False
        if request.method == "POST":
            update_picture_form = UpdatePictureForm(data=request.POST)
            if update_picture_form.is_valid():
                if 'picture' in request.FILES:
                    user_profile.picture = request.FILES['picture']
                    user_profile.save()
                    message = "Successfully changed!"
                else:
                    message = "Invalid attempt!"
            updated = True
            context_dict['update_message'] = message
    context_dict['updated'] = updated
    return render(request, 'radiu/myprofile.html', context=context_dict)

def search(request):
    context_dict = {}
    result_list = []
    if request.method == 'GET':
        starts_with = request.GET['suggestion'].strip()
        result_list = get_result_list(5, starts_with)
        for i in range(len(result_list)):
            song = result_list[i]
            context_dict[i] = {'title': str(song.title), 'artist': str(song.artist), 'slug': str(song.slug), 'id': song.id}
    return JsonResponse(context_dict)

def get_result_list(max_results=0, starts_with=''):
    result_list = []
    if starts_with:
        result_list = Song.objects.filter(title__istartswith=starts_with).order_by('title')
        if max_results > 0:
            if len(result_list) > max_results:
                result_list = result_list[:max_results]
    return result_list

def get_suggestions(request, fav_genre):
    songs = Song.objects.filter(genre=fav_genre).order_by('?')
    user_likes = Like.objects.filter(user=request.user)
    liked_songs = []
    for like in user_likes:
        liked_songs.append(like.song)
    suggested_songs = []
    for song in songs:
        if song not in liked_songs:
            if len(suggested_songs) < 5:
                suggested_songs.append(song)
            else:
                break
    return suggested_songs

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            context_dict = {'user_error': user_form.errors, 'profile_error': profile_form.errors}
            return render(request, 'radiu/register.html', context_dict)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    context_dict = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
    return render(request, 'radiu/register.html', context_dict)

@staff_member_required
def submit_song(request):
    submitted = False
    errors = False
    if request.method == 'POST':
        song_form = SongForm(request.POST)
        if song_form.is_valid():
            song = song_form.save()
            song.save()
            submitted = True
        else:
            errors = song_form.errors
    else:
        song_form = SongForm()
    context_dict = {'song_form': song_form, 'submitted': submitted, 'errors': errors}
    return render(request, 'radiu/submit_song.html', context_dict)

@staff_member_required
def add_artist(request):
    added = False
    errors = False
    if request.method == 'POST':
        artist_form = ArtistForm(request.POST)
        if artist_form.is_valid():
            artist = artist_form.save()
            artist.save()
            added = True
        else:
            errors = artist_form.errors
    else:
        artist_form = ArtistForm()
    context_dict = {'artist_form': artist_form, 'added': added, 'errors': errors}
    return render(request, 'radiu/add_artist.html', context_dict)

@staff_member_required
def delete_artist(request):
    deleted = False
    if request.POST['delete'] == 'yes':
        artist_id = request.POST['id']
        artist = Artist.objects.get(id=artist_id)
        songs = Song.objects.filter(artist=artist)
        for song in songs:
            profiles = UserProfile.objects.filter(favourite_song=song)
            for profile in profiles:
                profile.favourite_song = None
                profile.save()
        if Artist.objects.get(id=artist_id).delete():
            deleted = True
            message = 'Artist deleted successfully!'
        else:
            message = 'Failed to delete artist.'
    else:
        message = 'Error deleting artist!'
    context_dict = {'deleted': deleted, 'message': message}
    return render(request, 'radiu/artist.html', context_dict)

@staff_member_required
def delete_song(request):
    deleted = False
    if request.POST['delete'] == 'yes':
        song_id = request.POST['id']
        song = Song.objects.get(id=song_id)
        profiles = UserProfile.objects.filter(favourite_song=song)
        for profile in profiles:
            profile.favourite_song = None
            profile.save()
        if Song.objects.get(id=song_id).delete():
            deleted = True
            message = 'Song deleted successfully!'
        else:
            message = 'Failed to delete song.'
    else:
        message = 'Error deleting song!'

    context_dict = {'deleted': deleted, 'message': message}
    return render(request, 'radiu/song.html', context_dict)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return render(request, 'radiu/login.html', {"error": "Your Radi-U account is disabled."})
        else:
            return render(request, 'radiu/login.html', {"error": "Invalid login details supplied."})
    else:
        return render(request, 'radiu/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
