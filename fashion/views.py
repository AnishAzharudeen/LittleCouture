from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Category, Article

# Create your views here.
def index(request):
    return HttpResponse("Hi Fashion!")

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'fashion/category_list.html', {'categories': categories})

def article_list(request, category_id):
    articles = Article.objects.filter(category_id=category_id)
    return render(request, 'fashion/article_list.html', {'articles': articles})

class PostListView(ListView):
    model = Article
    template_name = 'fashion/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_on']

def lifestyle(request):
    post_list = Article.objects.filter(category__name='LifeStyle')
    return render(request, 'fashion/lifestyle.html', {'post_list': post_list})
