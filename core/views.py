from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Note, Collection, Comment
from .forms import CollectionForm, NoteForm
from imagekit import ImageSpec
from imagekit.processors import ResizeToFill
from django.utils import timezone



# Create your views here.
def homepage(request):
    return render(request, "core/homepage.html")

def add_collection(request):
    if request.method == 'GET':
        form = CollectionForm()
    else:
        form = CollectionForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect (to='list_collection')
    return render(request, "core/add_collection.html", {'form':form})

def list_collection (request):
    collection = Collection.objects.all()
    response = render(request, 'core/list_collection.html', {'collection': collection})
    return response

def add_note (request):
    if request.method == 'GET':
        form = NoteForm()
    else:
        form = NoteForm(request.POST, files=request.FILES)
        if form. is_valid():
            note = form.save(commit=False)
            print(note.collection)
            note.save()
            return redirect (to='homepage', collection_pk=note.collection.pk)
    return render (request, 'core/add_note.html', {'form':form})

    # def list_note (request, collection_pk):
    #     collection = get_object_or_404(Collection, pk=collection_pk)
    # return render(request, 'core/list_note.html', {'collection': collection, 'pk':collection_pk})

