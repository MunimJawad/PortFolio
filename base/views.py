from django.shortcuts import render,redirect
from .models import Project,Skill,Message,Endorsment,Comment
from .forms import ProjectForm,MessageForm,SkillForm,EndorsmentForm,CommentForm
from django.contrib import messages


def homePage(request):
    projects=Project.objects.all()[0:5]
    detailedSkills=Skill.objects.exclude(body='')
    skills=Skill.objects.filter(body='')
    endorsment=Endorsment.objects.filter(approved=True)
    form=MessageForm()

    if request.method == 'POST':
        form=MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your message was successfully sent.")



    context={'projects':projects, 'detailedSkills':detailedSkills, 
             'skills':skills, 'form':form,
             'endorsment':endorsment}
    return render(request,'base/home.html',context)

def projectPage(request,pk):
    project=Project.objects.get(id=pk)
    count=project.comment_set.count()

    comments=project.comment_set.all().order_by('-created')

    form=CommentForm()
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.project=project
            comment.save()
            messages.success(request,"Your message was successfully sent.")


    context={'project':project, 'count':count, 'comments':comments,
             'form':form}
    return render(request,'base/project.html',context)

def projectAll(request):

    projects=Project.objects.all()
    context={'projects':projects}
    return render(request,'base/projectAll.html',context)


def addProject(request):
    form=ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context= {'form':form}
    return render(request,'base/project_form.html',context)

def editProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/project_form.html', context)

def inboxPage(request):
    inbox=Message.objects.all().order_by('is_read')
    unreadCount=Message.objects.filter(is_read=False).count()
    context={'inbox':inbox, 'unreadCount':unreadCount}
    return render(request,'base/inbox.html',context)


def messagePage(request,pk):
    message=Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    context={'message':message}
    return render(request,'base/message.html',context)


def contactPage(request):
    form=MessageForm()
    if request.method == 'POST':
        form=MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your message was successfully sent.")

    context={'form':form}
    return render(request,'base/contact.html',context)


def addSkill(request):

    form=SkillForm()
    if request.method == 'POST':
        form=SkillForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}

    return render(request,'base/skill_form.html',context)


def deleteProject(request,pk):
    project=Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':project})

def deleteSkills(request,pk):
    skill=Skill.objects.get(id=pk)

    if request.method == 'POST':
        skill.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':skill})


def endorsment(request):
    form=EndorsmentForm()
    if request.method == 'POST':
        form=EndorsmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/endorsment.html',context)


def func(request):
    return render(request,'new/index.html')