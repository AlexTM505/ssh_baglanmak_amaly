from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieListApiView.as_view()),
    path('movies/<int:id>/', views.MovieDetailApiView.as_view()),
]
