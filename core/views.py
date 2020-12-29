from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Note, Collection, Comment
from .forms import CollectionForm
from imagekit import ImageSpec
from imagekit.processors import ResizeToFill


# Create your views here.
def homepage(request):
    return render(request, "core/homepage.html", {})

def add_collection(request):
    if request.method == 'GET':
        form = CollectionForm()
    else:
        form = CollectionForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect (to='list_collection')
    return render(request, "core/add_collection.html", {'form':form})