from django.db import models

class Song(models.Model):
	
	songId = models.IntegerField()
	name = models.CharField(max_length=100)
	releaseDate = models.DateField(null=True)
	kind = models.CharField(max_length=100, null=True)
	url = models.CharField(max_length=500, null=True)
	artistName = models.CharField(max_length=100, null=True)
	artistId = models.IntegerField(null=True)
	artistUrl = models.CharField(max_length=500, null=True)
	artworkUrl100 = models.CharField(max_length=500, null=True)
	genres = models.CharField(max_length=500, null=True)