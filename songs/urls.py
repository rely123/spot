from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from songs import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
	path('search/<str:pk>/', views.SongSearch.as_view(), name="songs_search"),
	path('list/', views.TopSongs.as_view(), name="songs_list"),
	path('delete/<int:pk>/', views.DeleteSong.as_view(), name="songs_delete"),
	path('add/', views.AddSong.as_view(), name="songs_add"),
	path('group/<str:pk>/', views.GroupByGen.as_view(), name="songs_group"),
	path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
]

urlpatterns = format_suffix_patterns(urlpatterns)