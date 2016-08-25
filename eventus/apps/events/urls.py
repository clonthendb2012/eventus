from django.conf.urls import patterns, url

urlpatterns = patterns('',
   url(r'^$', 'apps.events.views.index', name="index"),
   url(r'^panel/$', 'apps.events.views.main_panel', name="panel"),
   url(r'^panel/evento/nuevo$', 'apps.events.views.crear_evento', name="nuevo"),
   url(r'^panel/evento/(?P<evento_id>\d+)/$', 'apps.events.views.detalle_evento', name="detalle"),


)