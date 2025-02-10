from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.db.models import Count
from django.urls import reverse
from .models import Category, Article, Event, Comment
from .forms import CommentForm,ArticleForm




# Create your views here.
def index(request):
    return HttpResponse("Hi Fashion!")

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'fashion/category_list.html', {'categories': categories})

def article_list(request, category_id):
    articles = Article.objects.filter(category_id=category_id)
    return render(request, 'fashion/fashion.html', {'articles': articles})

class PostListView(ListView):
    model = Article
    template_name = 'fashion/post_list.html'
    context_object_name = 'post_list'
    ordering = ['-created_on']

class PostListView1(ListView):
    model = Article
    template_name = 'fashion/index.html'
    context_object_name = 'post_list'
    ordering = ['-created_on']


def lifestyle(request):
    post_list = Article.objects.filter(category__name='LifeStyle')
    return render(request, 'fashion/lifestyle.html', {'post_list': post_list})

def fashion(request):
    post_list = Article.objects.filter(category__name='Fashion')
    return render(request, 'fashion/fashion.html', {'post_list': post_list})

def post_detail(request, slug):
    queryset = Article.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.article = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
            return redirect('post_detail', slug=post.slug)
    else:
        comment_form = CommentForm()
    return render(request, 'fashion/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_count': comment_count,
        'comment_form': comment_form
    })

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Article.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.article = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))    


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Article.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))        

def event_list(request):
    event_list = Event.objects.all().order_by('-date')
    return render(request, 'fashion/event.html', {'event_list': event_list})

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'fashion/event_detail.html', {'event': event})

def like_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
    else:
        article.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))



def edit_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.user != article.author:
        messages.error(request, "You are not authorized to edit this article.")
        return redirect('post_detail', slug=slug)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "Article updated successfully.")
            return redirect('post_detail', slug=article.slug)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'fashion/edit_article.html', {'form': form, 'article': article})

def delete_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.user != article.author:
        messages.error(request, "You are not authorized to delete this article.")
        return redirect('post_detail', slug=slug)
    if request.method == "POST":
        article.delete()
        messages.success(request, "Article deleted successfully.")
        return redirect('home')
    return render(request, 'fashion/delete_article.html', {'article': article})
