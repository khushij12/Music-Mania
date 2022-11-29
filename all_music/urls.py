from django.urls import path
from . import views

# Add URLConf
urlpatterns = [
    path('playlist', views.playlist, name='playlist'),
    path('<int:id>',views.index,name='index'),
    path('create',views.add_playlist.as_view(),name='create')
]
