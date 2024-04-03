from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Project(models.Model):
    title= models.CharField(max_length=200)
    thumbnail= models.ImageField(null=True)
    body=RichTextUploadingField()
    slug=models.SlugField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)
    
    class Meta:
        ordering=['-created']

    def __str__(self):
        return self.title

class Skill(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    logo= models.ImageField(null=True,blank=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __self__(self):
        return self.title
    
class Tag(models.Model):
    name=models.CharField(null=True,max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)

    def __self__(self):
        return self.name
    


class Message(models.Model):
    name=models.CharField(null=True,max_length=200)
    email=models.CharField(null=True,max_length=200)
    subject=models.CharField(null=True,max_length=200)
    body=models.TextField()
    is_read=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)

    def __self__(self):
        return self.name
    

class Endorsment(models.Model):
    name = models.CharField(max_length=200,null=True)
    body=models.TextField()
    approved=models.BooleanField(default=False,null=True)
    featured = models.BooleanField(default=False)

    def __self__(self):
        return self.body[0:50]
    
class Comment(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.body[0:50]