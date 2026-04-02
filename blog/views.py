from django.shortcuts import render, redirect
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return redirect('/')
    return render(request, 'add_post.html')

def edit_post(request, id):
    post = Post.objects.get(id=id)

    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('/')

    return render(request, 'edit_post.html', {'post': post})

def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/')