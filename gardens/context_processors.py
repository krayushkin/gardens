'''
Created on 06.12.2010

@author: ATK
'''
import gardens.models as models
import gardens.forms as forms
import django.contrib.comments.models as cmnt
import django.contrib.auth.models as auth


def statistics(request):
    return {
   'gardens_count' : models.Kindergarden.objects.count(),
   'article_count' : models.Article.objects.count(),
   'comment_count' : cmnt.Comment.objects.count(),
   'user_count' : auth.User.objects.count(),

   }
    
