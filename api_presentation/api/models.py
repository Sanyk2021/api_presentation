from django.db import models


class AlbumSongs(models.Model):
    id = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class TheArtistOfTheSong(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(unique=True, max_length=75)
    author = models.ForeignKey(
        TheArtistOfTheSong,
        on_delete=models.CASCADE,
        related_name='albums',
        verbose_name='Исполнитель'
    )
    year = models.DateField()
    songs = models.ManyToManyField(
        AlbumSongs, through='SongsInAlbum'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'author'],
                name='unique_name_author'
            )
        ]

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=45, unique=True)
    album = models.ManyToManyField(
        AlbumSongs, through='SongsInAlbum'
    )

    def __str__(self):
        return self.title


class SongsInAlbum(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
