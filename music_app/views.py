from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *
import bcrypt
from django.contrib import messages
from django.db.models import Q
import requests
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os


def home(request):
    if request.session.get('user_id') != None:
        loggeduser = Users.objects.get(id=request.session['user_id'])
        context = {
            'playlists': Playlist.objects.filter(user_p=loggeduser),
            'allusers': Users.objects.exclude(id=request.session['user_id']),
            'allplaylists': Playlist.objects.exclude(user_p=loggeduser),
            'thisuser': loggeduser,


        }
        return render(request, 'home.html', context)
    return redirect('/')


def playlist_create(request):
    if request.session.get('user_id') != None:
        if request.method == 'POST':

            outcome = Playlist.objects.playlist_validator(request.POST)
            print(outcome[0])
            if len(outcome[0]) > 0:
                # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
                for key, value in outcome[0].items():
                    messages.error(request, value)
                    # redirect the user back to the form to fix the errors
                return redirect('/playlist_create')
            else:
                Playlist.objects.create(
                    name=request.POST['name'], description=request.POST['description'], user_p=Users.objects.get(id=request.session['user_id']))
                return redirect('/home')
        return render(request, 'playlist_create.html')
    return redirect('/')


def theplaylist(request, id):
    if request.session.get('user_id') != None:
        playlistid = id
        thisplaylist = Playlist.objects.get(id=playlistid)
        if request.method == "POST":
            outcome = Song.objects.song_validator(request.POST)
            if len(outcome[0]) > 0:
                # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
                for key, value in outcome[0].items():
                    messages.error(request, value)
                    # redirect the user back to the form to fix the errors
                return redirect('/theplaylist/'+id)
            else:
                myfile = request.FILES['myfile']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                song = Song.objects.create(
                    name=request.POST['name'], document=uploaded_file_url)
                thisplaylist.songs.add(song)
                thisplaylist.save()
                return redirect('/theplaylist/' + id)
        context = {
            "thisplaylist": thisplaylist,
            "songs": Song.objects.filter(song_playlist=thisplaylist),
            "comments": Comment.objects.filter(playlist=thisplaylist),

        }
        return render(request, 'theplaylist.html', context)

    return redirect("/")


def deletesong(request, id, thisplaylistid):
    if request.session.get('user_id') != None:
        songid = id
        thisong = Song.objects.get(id=songid)
        thisong_url = thisong.document
        thisong.delete()
        return redirect('/theplaylist/' + thisplaylistid)
    return redirect("/")


def otherplaylist(request, id):
    if request.session.get('user_id') != None:
        loggeduser = Users.objects.get(id=request.session.get('user_id'))
        playlistid = id
        thisplaylist = Playlist.objects.get(id=playlistid)
        print(thisplaylist.user_p.name)
        context = {
            "thisplaylist": thisplaylist,
            "songs": Song.objects.filter(song_playlist=thisplaylist),
            "comments": Comment.objects.filter(playlist=thisplaylist),
            "loggeduser": loggeduser,
            "userplaylists": loggeduser.user_playlist.all(),

        }
        return render(request, 'otherplaylist.html', context)
    return redirect("/")


def addsongtoplaylist(request, songid):
    if request.session.get('user_id') != None:
        song = Song.objects.get(id=songid)
        print(request.POST)
        playlist = Playlist.objects.get(id=request.POST['drop'])
        playlist.songs.add(song)
        return redirect('../theplaylist/' + request.POST['drop'])
    return redirect("/")


def comment(request, playlistid):
    if request.session.get('user_id') != None:
        if request.method == "POST":
            comment = Comment.objects.create(content=request.POST['comment'], user=Users.objects.get(
                id=request.session['user_id']), playlist=Playlist.objects.get(id=playlistid))
            return redirect('/theplaylist/others/' + playlistid)
        else:
            return HttpResponseNotFound("Nice Try")
    return redirect("/")


def commentdelete(request, commentid, thisplaylistid):
    thisplaylist = Playlist.objects.get(id=thisplaylistid)
    user = Users.objects.get(id=request.session.get('user_id'))
    if user == thisplaylist.user_p:
        thiscomment = Comment.objects.get(id=commentid)
        thiscomment.delete()
        return redirect('/theplaylist/' + thisplaylistid)
    elif user != thisplaylist.user_p and request.session.get('user_id') != None:
        thiscomment = Comment.objects.get(id=commentid)
        thiscomment.delete()
        return redirect('/theplaylist/others/' + thisplaylistid)
    return redirect("/")
