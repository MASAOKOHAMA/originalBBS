from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from .models import Article
from .forms import SearchForm
from .forms import ArticleForm


def index(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        articles = Article.objects.filter(content__contains=keyword)
    else:
        searchForm = SearchForm()
        articles = Article.objects.all()
    context = {
        'message': """Masao's First Work""",
        'articles': articles,
        'searchForm': searchForm,
    }
    print("index")
    return render(request, 'bbs/index.html', context)

def good(request, id):
    article = get_object_or_404(Article, pk=id)
    article.good_count += 1
    article.save()
    return redirect("bbs:index")

def favo(request, id):
    article = get_object_or_404(Article, pk=id)
    article.favorite += 1
    article.favorite %= 2
    article.save()
    favorite = get_object_or_404(Article, pk=id).favorite
    return redirect("bbs:index")

def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        articles = Article.objects.filter(content__contains=keyword)
    else:
        searchForm = SearchForm()
        articles = Article.objects.all()
    context = {
        'message': 'Delete Article ' + str(id),
        'articles': articles,
        'searchForm': searchForm,
    }
    return render(request, 'bbs/index.html', context)

def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    articleForm = ArticleForm(instance=article)
    context = {
        'message': 'Show Article ' + str(id),
        'article': article,
        'articleForm': articleForm,
    }
    return render(request, 'bbs/detail.html', context)

def new(request):
    articleForm = ArticleForm()
    context = {
        'message': 'New Article',
        'articleForm': articleForm,
    }
    return render(request, 'bbs/new.html', context)

class ArticleCreate(CreateView):
    template_name = 'bbs/new.html'
    model = Article
    fields = ('images', 'content', 'user_name')
    success_url = reverse_lazy("bbs:index")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)


class ArticleUpdate(UpdateView, id):
    template_name = 'bbs/new.html'
    model = Article
    fields = ('images', 'content', 'user_name')
    success_url = reverse_lazy("bbs:index")

    def get_success_url(self):
        return reverse('bbs:index', kwargs={'id': self.article.id})

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super(UpdateView, self).form_valid(form)

def edit(request, id):
    article = get_object_or_404(Article, pk=id)
    articleForm = ArticleForm(instance=article)
    context = {
        'message': 'Edit Article',
        'article': article,
        'articleForm': articleForm,
    }
    return render(request, 'bbs/edit.html', context)

def update(request, id):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=id)
        articleForm = ArticleForm(request.POST, instance=article)
        if articleForm.is_valid():
            articleForm.save()
    context = {
        'message': 'Update article ' + str(id),
        'article': article,
        'articleForm': articleForm,
    }
    return render(request, 'bbs/detail.html', context)