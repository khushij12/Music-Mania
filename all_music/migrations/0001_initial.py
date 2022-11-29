# Generated by Django 4.1 on 2022-11-28 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("authentication", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Song",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField()),
                ("artist", models.TextField()),
                ("image", models.ImageField(upload_to="")),
                ("audio_file", models.FileField(blank=True, null=True, upload_to="")),
                ("audio_link", models.CharField(blank=True, max_length=200, null=True)),
                ("duration", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Playlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("playlist_name", models.CharField(max_length=200)),
                ("image", models.ImageField(upload_to="")),
                (
                    "song",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="all_music.song"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="authentication.userinfo",
                    ),
                ),
            ],
        ),
    ]