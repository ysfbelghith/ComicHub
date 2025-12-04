from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

# Liste des posts
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

# Détail d'un post
def detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/detail.html', {'post': post})

# Ajouter un post
def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST.get('author', 'Anonyme')  # ← RÉCUPÉRER L'AUTEUR
        Post.objects.create(title=title, content=content, author=author)
        return redirect('home')
    return render(request, 'blog/add.html')

# Modifier un post
def edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.author = request.POST.get('author', post.author)  # ← MODIFIER L'AUTEUR
        post.save()
        return redirect('detail', id=post.id)
    return render(request, 'blog/modifier.html', {'post': post})

# Supprimer un post
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('home')