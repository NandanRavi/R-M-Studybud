from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth.decorators import login_required

from .models import Project, Tag
from .forms import ProjectForm
from .utils import searchProjects
def projects(request):
    projects, search_query = searchProjects(request)



    context = {'projects':projects, 'search_query':search_query}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    context = {'project':projectObj}
    return render(request, 'projects/single_project.html', context)

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')
    context = {'form':form}
    return render(request, 'projects/project_forms.html', context)

@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES , instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form':form}
    return render(request, 'projects/project_forms.html', context)

@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context ={'object':project}
    return render(request, 'delete_template.html',context)

