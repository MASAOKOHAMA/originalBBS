from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('content', 'user_name', 'good_count', 'images')

class SearchForm(forms.Form):
    keyword = forms.CharField(label='Search', max_length=100)