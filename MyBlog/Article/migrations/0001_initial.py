# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe9\xa2\x98')),
                ('author', models.CharField(max_length=32, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
                ('time', models.DateField(verbose_name=b'\xe5\x8f\x91\xe8\xa1\xa8\xe6\x97\xa5\xe6\x9c\x9f')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('pic', models.ImageField(upload_to=b'images', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x9b\xbe\xe7\x89\x87')),
                ('num', models.IntegerField(verbose_name=b'\xe9\x98\x85\xe8\xaf\xbb\xe6\xac\xa1\xe6\x95\xb0')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32, verbose_name=b'\xe7\x85\xa7\xe7\x89\x87\xe6\xa0\x87\xe9\xa2\x98')),
                ('src', models.ImageField(upload_to=b'images', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe9\x93\xbe\xe6\x8e\xa5')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b\xe5\x90\x8d\xe7\xa7\xb0')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
        ),
        migrations.AddField(
            model_name='picture',
            name='types',
            field=models.ForeignKey(to='Article.Type'),
        ),
        migrations.AddField(
            model_name='article',
            name='types',
            field=models.ForeignKey(to='Article.Type'),
        ),
    ]
