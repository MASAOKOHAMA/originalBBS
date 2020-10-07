from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('content', 'user_name')
    # content = forms.CharField(label='新規', max_length=100)
    # user_name = forms.CharField(label='新規', max_length=100)

class SearchForm(forms.Form):
    keyword = forms.CharField(label='検索', max_length=100)