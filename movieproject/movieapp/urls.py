from . import views
from django.urls import path, include
app_name='movieapp'
urlpatterns = [
    path('',views.movies,name='movies'),
    path('movie/<int:movie_id>/',views.dtails,name='dtails'),
    path('add/',views.addmovie,name='addmovie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
    ]