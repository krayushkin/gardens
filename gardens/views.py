# -*- encoding: utf8 -*-
# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic.list_detail import object_detail, object_list
from django.template import RequestContext 
from gardens.context_processors import statistics

import models
import forms
import json



def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))

def choose(request):
    coord = []
    for g in models.Kindergarden.objects.all():
        coord.append( {"g_id": g.id, "coord" : [g.lng, g.lat], "name" : g.name } )
    return render_to_response('choose.html', dictionary={"coord" : json.dumps(coord)}, context_instance=RequestContext(request))

def garden_details(request, id):
    return object_detail(request, models.Kindergarden.objects.all(), object_id=id, template_name='garden_details.html')

def kindergardens(request):
    return object_list(request=request, queryset=models.Kindergarden.objects.all(), template_name='kindergardens.html')

def article(request, id):
    return object_detail(request, models.Article.objects.all(), object_id=id, template_name='article.html')

def admin_garden_list(request):
    return object_list(request, models.Kindergarden.objects.all(), template_name='admin/garden_list.html')

def admin_article_list(request):
    return object_list(request, models.Article.objects.all(), template_name='admin/article_list.html')

def admin_user_list(request):
    return object_list(request, models.User.objects.all(), template_name='admin/user_list.html')

# forms
def admin_garden_add(request):
    return render_to_response('admin/garden_add_form.html', context_instance=RequestContext(request))

def admin_user_add(request):
    return render_to_response('admin/user_add_form.html', context_instance=RequestContext(request))


def admin_article_add(request):
    
    form = forms.AddEditArticle()
    return render_to_response('admin/article_add_form.html', {'form' : form}, context_instance=RequestContext(request))


def admin_garden_edit(request, id):
    pass

def admin_user_edit(request, id):
    pass

def admin_article_edit(request, id):
    pass
