from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('content', 'user_name')

class SearchForm(forms.Form):
    keyword = forms.CharField(label='検索', max_length=100)