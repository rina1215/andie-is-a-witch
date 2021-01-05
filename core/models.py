from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.processors import ResizeToFit, ResizeToFill
from imagekit.models import ImageSpecField
from django.utils import timezone
from django.conf import settings


class User(AbstractUser):
    pass



class Collection (models.Model):
    collection_by = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name="collections")
    title = models.CharField(max_length=100, null=False, blank=False)
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    public_collection = models.BooleanField(default=True)
    note_image = models.ImageField(upload_to='collection', null=True)
    note_image_thumb = ImageSpecField(source="note_image", processors=[ResizeToFill(200,200)], format="JPEG", options={'quality': 80})
    note_image_large = ImageSpecField(source="note_image", processors=[ResizeToFit(600,600)], format="JPEG", options={"quality": 90})

    def __str__(self):
        return f'{self.title}'
    
class Note(models.Model):
    note_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="notes", null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=False)
    note = models.ImageField(upload_to="collection", null=True, blank=True)
    note_thumb = ImageSpecField(source="note", processors=[ResizeToFill(200,200)], format="JPEG", options={'quality': 80})
    note_large = ImageSpecField(source="note", processors=[ResizeToFit(600,600)], format="JPEG", options={"quality": 90})
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    public_note = models.BooleanField(default=True)
    collection_of_notes = models.ForeignKey(to=Collection, on_delete = models.CASCADE, related_name='collections', null=True, blank=True) 



    def __str__(self):
        return f'{self.title}'

class Comment (models.Model):
    comment_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    comments = models.ForeignKey(to=Note, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    body = models.TextField(null=False, blank =False)
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)


    def __str__(self):
        return f'{self.owner}'