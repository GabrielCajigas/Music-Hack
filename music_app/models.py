from __future__ import unicode_literals
import os
from django.conf import settings
from django.db.models import Q
from django.db.models import FileField
from django.apps import apps
from django.core.management.base import BaseCommand
from django.db import models
import re
import bcrypt
from login_app.models import *
from datetime import datetime


class PlaylistManager(models.Manager):
    def playlist_validator(self, postData):
        outcome = [{},
                   None]
        if len(postData['name']) < 1:
            outcome[0]["name"] = "Name needs to be at least 1 characters"
        if len(postData['description']) < 10:
            outcome[0]["description"] = "Description needs to be at least 10 characters"
        return outcome


class SongManager(models.Manager):
    def song_validator(self, postData):
        outcome = [{},
                   None]
        if len(postData['name']) < 1:
            outcome[0]["name"] = "Name needs to be at least 1 characters"
        return outcome


class Song(models.Model):
    name = models.CharField(max_length=25)
    document = models.FileField(
        upload_to='documents/')
    objects = SongManager()


class Playlist(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=55)
    songs = models.ManyToManyField(
        Song, related_name="song_playlist")
    user_p = models.ForeignKey(
        Users, related_name="user_playlist", on_delete=models.CASCADE)
    objects = PlaylistManager()


class Comment(models.Model):
    content = models.TextField(max_length=max)
    user = models.ForeignKey(
        Users, related_name="comments", on_delete=models.CASCADE)
    playlist = models.ForeignKey(
        Playlist, related_name="comments", on_delete=models.CASCADE)
