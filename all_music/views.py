# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import CreateView
# imported our models
from django.core.paginator import Paginator
from . models import Song,Playlist
from authentication.models import userInfo


def index(request,id):
    pl = Playlist.objects.get(pk=id)
    song_ = pl.song.all()
    paginator= Paginator(song_,1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"index.html",context)

def playlist(request):
    user_ = userInfo.objects.filter(is_login=True)
    context_object={}
    if user_:
        pl = Playlist.objects.filter(user = user_[0])
        context_object['pl']=pl
    else:
        redirect('login')

    return render(request,'playlist1.html',context_object)

class add_playlist(CreateView):
    model = Playlist
    fields='__all__'
    template_name = 'create_playlist.html'
    success_url = 'playlist'