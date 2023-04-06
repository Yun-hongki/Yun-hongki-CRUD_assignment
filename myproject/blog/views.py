from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs' : blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog' : blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.author = request.POST['author']
    blog.content = request.POST['content']
    blog.image = request.FILES.get('image')
    blog.save()
    return redirect('detail', blog.id)

def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'blog' : blog})

def update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.title = request.POST['title']
    blog.author = request.POST['author']
    blog.content = request.POST['content']
    blog.save()
    return redirect('detail', blog.id)

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('index')