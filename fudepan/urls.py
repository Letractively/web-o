from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from fudepan import settings
from website.views import *
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^contacto/?$', ContactoView.as_view(), name='contacto'),
    url(r'^que-hacemos/?$', QueHacemosView.as_view(), name='que-hacemos'),
    url(r'^como-colaborar/?$', ComoColaborarView.as_view(), name='como-colaborar'),
    url(r'^quienes-somos/?$', QuienesSomosView.as_view(), name='quienes-somos'),
    url(r'^quienes-colaboran/?$', ColaboradoresView.as_view(), name='colaboradores'),
    url(r'^member/([^/]+)/?$', MemberView.as_view(), name='member'),
    url(r'^nuestros-logros/?$', NuestrosLogrosView.as_view(), name='nuestros-logros'),
    url(r'^projects/?$', ProjectsView.as_view(), name='projects'),
    url(r'^projects/([^/]+)/?$', ProjectView.as_view(), name='project'),
    url(r'^publications/?$', PublicationsView.as_view(), name='publications'),
    url(r'^publications/([^/]+)/?$', PublicationView.as_view(), name='publication'),
    url(r'^notice/$', notices, kwargs={'id':None}, name='notices'),
    url(r'^notice/(?P<id>\d+)$', notices, name='notice'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^openid/', include('django_openid_auth.urls')),
    url(r'^logout/?$', 'django.contrib.auth.views.logout'),
    url(r'^error500/?$', Error500.as_view()),
    url(r'^error404/?$', Error404.as_view()),
)

if settings.DEBUG:
    urlpatterns += patterns('',
          url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
             'document_root': settings.MEDIA_ROOT,
             }),
          )
