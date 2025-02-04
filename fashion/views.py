from django.shortcuts import render
from django.http import HttpResponse
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
