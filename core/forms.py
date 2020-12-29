from django import forms
from .models import Note, Collection, Comment

class CollectionForm(forms.ModelForm):
    private = forms.BooleanField(widget=forms.CheckboxInput, required=False)

    class Meta:
        model = Collection
        fields = [
            'collection_by',
            'title',
            'public_collection',

        ]