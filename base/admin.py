from django.contrib import admin

# Register your models here.
from .models import Project,Skill,Tag,Message,Endorsment,Comment

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Tag)
admin.site.register(Message)
admin.site.register(Endorsment)
admin.site.register(Comment)


