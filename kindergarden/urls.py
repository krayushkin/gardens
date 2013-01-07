from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to
from django.views.static import serve
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from gardens.context_processors import statistics
import gardens.views as views
import kindergarden.settings as settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', redirect_to, {'url' : '/home/'}),
    (r'^home/$', views.home),

    (r'^choose/$', views.choose),
    
    #list of gardens
    (r'^kindergardens/$', views.kindergardens),
    
    #garden details
    (r'^kindergardens/(?P<id>\d+)/$',  views.garden_details),
    
    #article
    (r'^article/(?P<id>\d+)/$',  views.article),
    

    (r'^comments/', include('django.contrib.comments.urls')),

    
#-----------------ADMIN------------------------------------------------------------------------------------------ 

    # Example:
    # (r'^kindergarden/', include('kindergarden.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
