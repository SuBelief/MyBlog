#coding:utf-8
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=32,verbose_name="类型名称")
    description = RichTextUploadingField(verbose_name="类型描述")

    def __unicode__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=32,verbose_name="文章标题")
    author = models.CharField(max_length=32,verbose_name="作者")
    time = models.DateField(verbose_name="发表日期")
    content = RichTextUploadingField(verbose_name="文章内容")
    description = RichTextUploadingField(verbose_name="文章描述")
    pic = models.ImageField(upload_to="images",verbose_name="文章图片")
    num = models.IntegerField(verbose_name="阅读次数")
    types = models.ForeignKey(to="Type",to_field="id")

    def __unicode__(self):
        return self.title

class Picture(models.Model):
    title = models.CharField(max_length=32,verbose_name="照片标题")
    src = models.ImageField(upload_to="images",verbose_name="图片链接")
    types = models.ForeignKey(to ="Type",to_field="id")

    def __unicode__(self):
        return self.title