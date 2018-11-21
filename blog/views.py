from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings

from .models import Article, Category
from .forms import ArticleForm, CategoryForm


def username_check(user):
    return user.username == settings.USER_ADMIN


def home(request):
    articles = Article.objects.all()
    return render(request, 'blog/home.html', context={'articles': articles})


@user_passes_test(username_check)
@login_required(login_url='users:login')
def create_article(request):
    if request.method != 'POST':
        form = ArticleForm()
    else:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.owner = request.user
            new_article.save()
            return HttpResponseRedirect(reverse('blog:latest_article'))
    context = {'form': form}
    return render(request, 'blog/create_article.html', context)


def read_article(request, article_title):
    article = Article.objects.get(title=article_title)
    context = {'article': article}
    return render(request, 'blog/read_article.html', context)


@user_passes_test(username_check)
@login_required(login_url='users:login')
def update_article(request, article_title):
    article = Article.objects.get(title=article_title)
    category_ = article.category
    if article.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = ArticleForm(instance=article)
    else:
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('blog:category', args=[category_.name]))
    context = {'article': article, 'form': form}
    return render(request, 'blog/update_article.html', context)


@login_required(login_url='users:login')
def latest_article(request):
    article = Article.objects.order_by('-date_created')[0]
    context = {'article': article}
    return render(request, 'blog/read_article.html', context)


@user_passes_test(username_check)
@login_required(login_url='users:login')
def delete_article(request, article_title):
    article = get_object_or_404(Article, title=article_title)
    category = article.category
    if article.owner != request.user:
        raise Http404
    if request.method == 'POST':
        article.delete()
        return HttpResponseRedirect(reverse('blog:category', args=[category.name]))


@user_passes_test(username_check)
@login_required(login_url='users:login')
def create_category(request):
    if request.method != 'POST':
        form = CategoryForm()
    else:
        form = CategoryForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('blog:categories'))
    context = {'form': form}
    return render(request, 'blog/create_category.html', context)


@login_required(login_url='users:login')
def category(request, category_name):
    category_ = Category.objects.get(name=category_name)
    articles = category_.article_set.order_by('-date_created')
    articles = pager(request, articles)
    context = {'category': category, 'articles': articles}
    return render(request, 'blog/category.html', context)


@login_required(login_url='users:login')
def categories(request):
    list_categories = Category.objects.all()
    context = {'categories': list_categories}
    return render(request, 'blog/categories.html', context)


def pager(request, articles):
    page = request.GET.get('page', 1)

    paginator = Paginator(articles, 2)
    try:
        articles = paginator.get_page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return articles


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')
