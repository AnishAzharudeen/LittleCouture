from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Category, Article, Event

# Create your views here.
def index(request):
    return HttpResponse("Hi Fashion!")

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'fashion/category_list.html', {'categories': categories})

def article_list(request, category_id):
    articles = Article.objects.filter(category_id=category_id)
    return render(request, 'fashion/fashion.html', {'articles': articles})

def PostListView(ListView):
    model = Article
    template_name = 'fashion/post_list.html'
    context_object_name = 'post_list'
    ordering = ['-created_on']

def lifestyle(request):
    post_list = Article.objects.filter(category__name='LifeStyle')
    return render(request, 'fashion/lifestyle.html', {'post_list': post_list})

def fashion(request):
    post_list = Article.objects.filter(category__name='Fashion')
    return render(request, 'fashion/fashion.html', {'post_list': post_list})

def post_detail(request, slug):
    post = get_object_or_404(Article, slug=slug)
    return render(request, 'fashion/post_detail.html', {'post': post})

def event_list(request):
    event_list = Event.objects.all().order_by('-date')
    return render(request, 'fashion/event.html', {'event_list': event_list})

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'fashion/event_detail.html', {'event': event})
