from django import forms
from .models import Article
from .models import Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('content', 'user_name', 'good_count', 'images')

class SearchForm(forms.Form):
    keyword = forms.CharField(label='Search', max_length=100)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)