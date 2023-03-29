from django.shortcuts import render,redirect
from app1.models import *
from django.contrib import messages
def allshows(request):
    context={
        'allshows':Show.objects.all()
    }
    return render(request,'allshows.html',context)

def create_show(request):
    return render(request,'create_show.html')

def handle_form(request):
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('shows/new')
    else:
        Show.objects.create(title=request.POST['title'],network=request.POST['network'],release_date=request.POST['release_date'],description=request.POST['description'])
        id=Show.objects.last().id
    return redirect('shows/'+str(id))

def show_details(request,id):
    context={
        'show':Show.objects.get(id=id)
    }
    return render(request,'show_details.html',context)


def edit_show(request,id):

    context={
        'show':Show.objects.get(id=id)
    }
    return render(request,'edit_show.html',context)

def update_show(request,id):

    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('shows/new')
    else:
        show=Show.objects.get(id=id)
        show.title=request.POST['title']
        show.network=request.POST['network']
        show.release_date=request.POST['release_date']
        show.description=request.POST['description']
        show.save()
    return redirect('/shows/'+str(id))

def delete_show(request,id):
    show=Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')


# Create your views here.
