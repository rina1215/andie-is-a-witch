from django import forms
from .models import Note, Collection, Comment

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = [
            'collection_by',
            'title',
            'public_collection',
            'note_image',

        ]

class NoteForm(forms.ModelForm):
    
    class Meta:
        model = Note
        fields = [
            'note_by',
            'note',
            

        ]
      