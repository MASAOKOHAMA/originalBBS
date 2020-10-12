from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article
from .forms import SearchForm
from .forms import ArticleForm
# from .forms import CountForm


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

def good(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # if request.method == '':
    article.good_count += 1
    article.save()
    print("good")
    print(article)
    print(article.good_count)
    good_count = get_object_or_404(Article, pk=pk).good_count
    # context = {
    #     'count': good_count
    # }
    #####
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        articles = Article.objects.filter(content__contains=keyword)
    else:
        searchForm = SearchForm()
        articles = Article.objects.all()
    context = {
        'message': 'Good Article ' + str(pk),
        'articles': articles,
        'searchForm': searchForm,
        'count': good_count
    }
    #####
    return render(request, 'bbs/index.html', context)

def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    context = {
        'message': 'Show Article ' + str(id),
        'article': article,
    }
    return render(request, 'bbs/detail.html', context)



def create(request):
    if request.method == 'POST':
        articleForm = ArticleForm(request.POST)
        if articleForm.is_valid():
            article = articleForm.save()

    context = {
        # 'message': 'Create article ' + str(article.id),
        'message': 'Create Article ',
        'article': article,
    }
    return render(request, 'bbs/detail.html', context)

def new(request):
    articleForm = ArticleForm()

    context = {
        'message': 'New Article',
        'articleForm': articleForm,
    }
    return render(request, 'bbs/new.html', context)

# def new(request):
#     if request.method == 'POST':
#         articleForm = ArticleForm(request.POST)
#         if articleForm.is_valid():
#             article = articleForm.save()
#
#     context = {
#         'message': 'Create article ' + str(article.id),
#         'articleForm': articleForm,
#         'article': article,
#     }
#     return render(request, 'bbs/new.html', context)

def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()
    # articles = Article.objects.all()
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
        'message': 'Update Article ' + str(id),
        'article': article,
    }
    return render(request, 'bbs/detail.html', context)