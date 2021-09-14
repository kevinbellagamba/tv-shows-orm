from tv_app.models import Show
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
def index(request):     
    context = {
        'shows' : Show.objects.all(),
    }
    return render(request, "index.html", context)

def creation(request):
    return render(request, 'addShow.html')

def addShow(request):
    Show.objects.create(
    title=request.POST['title'], 
    network=request.POST['network'], 
    release_date=request.POST['release_date'], 
    description=request.POST['description'], 
    )
    return redirect("/shows")

def viewShow(request, show_id):
    context = {
        'show' : Show.objects.get(id=show_id)
    }
    return render(request, 'displayShow.html', context)

def editShow(request, show_id):
    context = {
        'show' : Show.objects.get(id=show_id)
    }
    return render(request, 'editShow.html', context)

def updateShow(request):
    update = Show.objects.get(id=request.POST['ID'])
    update.title = request.POST['title']
    update.network = request.POST['network']
    update.release_date = request.POST['release_date']
    update.description = request.POST['description']
    update.save()
    return redirect("/shows")

def deleteShow(request, show_id):
    delete = Show.objects.get(id=show_id)
    delete.delete()
    return redirect('/shows')


