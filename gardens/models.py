# -*- coding: utf8 -*-

from django.db import models
import json

class Kindergarden(models.Model):
    name = models.CharField(u'Название детского сада', max_length=200)
    lng = models.FloatField('Долгота в градусах')
    lat = models.FloatField('Широта в градусах')
    address = models.CharField('Адрес', max_length=200)
    telephone = models.CharField('Телефон', max_length=200)
    rst_description = models.TextField('Описание сада в формате RST')
    
    def js_lat(self):
        return json.dumps(self.lat)
        
    def js_lng(self):
        return json.dumps(self.lng)
        
    
    def __unicode__(self):
        return unicode(self.name)
        

class Gallery(models.Model):
    image = models.FileField('Изображение', upload_to='.')
    kindergarden = models.ForeignKey(Kindergarden, verbose_name='Для какого детского сада')
    description = models.TextField('Описание фотографии')
    
    def __unicode__(self):
        return self.image.name

class User(models.Model):
    login = models.CharField('Логин', max_length=200)
    password = models.CharField('Пароль', max_length=200)
    admin = models.BooleanField('Админь?')

    def __unicode__(self):
        return self.login

class Article(models.Model):
    kindergarden = models.ForeignKey(Kindergarden, verbose_name='Для какого детского сада')
    title = models.CharField('Заголовок', max_length=1000)
    rst_content = models.TextField('Содержание статьи в формате RST')

    def __unicode__(self):
        return self.title
    
class GalleryComment(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь')
    gallery = models.ForeignKey(Gallery, verbose_name='К какой фотографии')
    rst_comment = models.TextField('Комментарий в формате RST')
    
    def __unicode__(self):
        return u"{0} | {1}".format(self.user, self.gallery)
    
class ArticleComment(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь')
    article = models.ForeignKey(Article, verbose_name='К какой статье')
    rst_comment = models.TextField('Комментарий в формате RST')

    def __unicode__(self):
        return u"{0} | {1}".format(self.user, self.article)

# Create your models here.
