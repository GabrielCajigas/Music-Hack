# Generated by Django 2.0.7 on 2019-09-19 15:09

from django.db import migrations, models
import music_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0004_auto_20190919_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='document',
            field=models.FileField(upload_to='documents/', validators=[music_app.validators.validate_file_extension]),
        ),
    ]
