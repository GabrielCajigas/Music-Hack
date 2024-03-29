# Generated by Django 2.0.7 on 2019-09-19 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
        ('music_app', '0003_playlist_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='user',
        ),
        migrations.AddField(
            model_name='playlist',
            name='user_p',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_playlist', to='login_app.Users'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(related_name='song_playlist', to='music_app.Song'),
        ),
    ]
