from django.conf.urls import patterns, url


urlpatterns = patterns('',
   url(regex=r'^$', view='core.views.main', name='main'),

)

