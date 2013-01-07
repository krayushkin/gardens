#-*- coding: utf-8 -*-
'''
Created on 07.12.2010

@author: Dmitry
'''

import django.forms as forms

class LoginForm(forms.Form):
    login = forms.CharField(widget = forms.TextInput(attrs={'size':'14'}))
    password = forms.CharField( widget = forms.PasswordInput(attrs={'size':'14'}) )
    
class Comment(forms.Form):
    content = forms.CharField()
    
class Register(forms.Form):
    login = forms.CharField()
    password = forms.CharField()
    
class AddEditArticle(forms.Form):
    title = forms.CharField()
    rst_content = forms.CharField()
    
class AddEditGarden(forms.Form):
    pass