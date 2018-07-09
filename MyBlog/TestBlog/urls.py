"""TestBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Article.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/',include("ckeditor_uploader.urls")),
    url(r'^$', articles),
    url(r'^index.html/$', index),
    url(r'^about.html/$', about),
    # url(r'^listpic.html/$', listpic),
    url(r'^newslistpic/$', newslistpic),
    url(r'^newslistpic/(\d+)', newslistpic),
    url(r'^articles/$',articles),
    url(r'^articles/(\d+)', articles),
    url(r'^article/(\d+)', article),
    url(r'^picture/$', picture),
    url(r'^picture/(\d+)', picture),
    url(r'^newlistpic/$', newlistpic),
    url(r'^newlistpic/(\d+)', newlistpic),
]
