# advanced_features_and_security/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Article

@login_required
def article_list(request):
    if request.user.has_perm('advanced_features_and_security.can_view'):
        articles = Article.objects.all()
        return render(request, 'article_list.html', {'articles': articles})
    else:
        return HttpResponseForbidden("You do not have permission to view articles.")

@permission_required('advanced_features_and_security.can_create', raise_exception=True)
def article_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Article.objects.create(title=title, content=content)
        return redirect('article_list')
    return render(request, 'article_create.html')

@permission_required('advanced_features_and_security.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('article_list')
    return render(request, 'article_edit.html', {'article': article})

@permission_required('advanced_features_and_security.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')

# Create your views here.
