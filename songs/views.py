from rest_framework.views import APIView
from django.shortcuts import render
from songs.models import Song
from rest_framework.response import Response
from songs.serializers import SongSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

#Search song by name
class SongSearch(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request, pk, format=None):
		sql = "SELECT * FROM songs_song WHERE name LIKE '%"+pk+"%'"
		songs = Song.objects.raw(sql)
		serializer = SongSerializer(songs, many=True, read_only=True)
		return Response(serializer.data)

#List the top 50 songs
class TopSongs(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request, format=None):
		songs = Song.objects.raw("SELECT * FROM songs_song LIMIT 50")
		serializer = SongSerializer(songs, many=True, read_only=True)
		return Response(serializer.data)

#Remove song by song id
class DeleteSong(APIView):
	permission_classes = (IsAuthenticated,)
	def delete(self, request, pk, format=None):
		try:
			song_object = Song.objects.get(songId=pk)
			song_object.delete()
			return Response({'message': 'Song Deleted'}, status=status.HTTP_200_OK)
		except Song.DoesNotExist:
			song_object = None
			return Response({'error_message': 'Song does not exist'}, status=status.HTTP_400_BAD_REQUEST)

#Add new track
class AddSong(APIView):
	permission_classes = (IsAuthenticated,)
	def post(self, request, format=None):
		serializer = SongSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Group songs by genres
class GroupByGen(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request, pk, format=None):
		sql = "SELECT * FROM songs_song WHERE genres LIKE '%"+pk+"%'"
		songs = Song.objects.raw(sql)
		serializer = SongSerializer(songs, many=True, read_only=True)
		return Response(serializer.data)

