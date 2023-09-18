from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.
def movies(request):
    movie=Movie.objects.all()
    context={'movie_list':movie}
    return render(request,'home.html',context)

def dtails(request,movie_id):
    movie=Movie.objects.get(id=movie_id)

    return render(request,'details.html',{'movie':movie})
def addmovie(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        disc = request.POST.get('desc','')
        year = request.POST.get('year','')
        img =  request.FILES['img']

        movie =Movie(name=name,desc=disc,year=year,img=img)
        movie.save()
    return render(request,'add.html')
#to add
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

#to delete
def delete(request,id):
    if request.method =="POST":
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')


