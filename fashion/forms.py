from .models import Comment,Article
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'slug', 'author', 'featured_image', 'content', 'excerpt', 'category'] 