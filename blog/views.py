from django.shortcuts import render,HttpResponse
from .models import *
from django.contrib import messages


# Create your views here.

def index(request):
    
    return render(request, 'index.html')

def blog(request):
    blogs=Blog.objects.all()
    context={'blogs':blogs}
    return render(request,'blog.html',context)

def blogpost(request,slug):
    blog=Blog.objects.filter(slug=slug).first()
    context={'blog':blog}
    if request.method == 'POST':
        
        comment=request.POST['comment']
        ins=Comment(comment=comment)
        ins.save()
    return render(request,'blogpost.html',context)   
    

def search(request):
    query = request.POST['query']
    if len(query)>78:
        allposts=Blog.objects.none()
    else:
        allposts_T=Blog.objects.filter(title__icontains=query)
        allposts_C=Blog.objects.filter(content__icontains=query)
        allposts=allposts_T.union(allposts_C)
    
    params={'allposts':allposts,'query':query}
    return render(request,'search.html',params)


def profile(request):
    details=Profile.objects.all()
    context={'details':details}
    return render(request,'profile.html',context)





    