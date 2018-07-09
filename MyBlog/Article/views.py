#coding:utf-8
from django.shortcuts import render_to_response
from models import *
from django.core.paginator import Paginator

# Create your views here.
def articles(request,page=1):

    page = int(page)
    article_list = Article.objects.all()
    Articles = Paginator(article_list,2)
    articleList = Articles.page(page)
    return render_to_response("articles.html",locals())

def article(request,ids):
    ids = int(ids)
    try:
         article = Article.objects.get(id = ids)
    except:
        return  render_to_response("404.html")
    else:return render_to_response("article.html",locals())

def index(request):
    # types = Type.objects.get(id = 4)
    # articleList  = types.article_set.all()

    articleList = Article.objects.all()
    return render_to_response("index.html",locals())

def about(request):
    return render_to_response("about.html")

# def listpic(request):
#     return render_to_response("listpic.html")

def newslistpic(request,page=1):
    page = int(page)
    types = Type.objects.get(id = 1)
    article_list = types.article_set.all()
    Articles = Paginator(article_list,2)
    articleList = Articles.page(page)
    return render_to_response("newslistpic.html",locals())

def picture(request,page=1):
    page = int(page)
    article_list = Article.objects.all()
    Articles = Paginator(article_list,8)
    articleList = Articles.page(page)
    return render_to_response("picture.html",locals())

def newlistpic(request,page=1):
    page = int(page)
    types = Type.objects.get(id = 4)
    article_list = types.article_set.all()
    Articles = Paginator(article_list,2)
    articleList = Articles.page(page)
    return render_to_response("newlistpic.html",locals())
