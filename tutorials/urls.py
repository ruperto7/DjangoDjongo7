from django.conf.urls import url 
from tutorials import views
from tutorials import views_debug
#
#import debug_toolbar
from django.urls import path, include
from django.conf import settings
import logging, logging.config #LOGGER
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import views as sitemaps_views
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
#

urlpatterns = [ 
    path('', views.root, name='root'),
    url(r'home', views.home, name='home'),
    url(r'misc2', views.misc2, name='misc2'), 
    url(r'misc', views.misc, name='misc'),
    url(r'^admin/', admin.site.urls, name='admin'),
    path('index',  TemplateView.as_view(template_name="index.html", extra_context={'title':'Custom Title'} )),
    path('accounts/', include('django.contrib.auth.urls')),
    path('views_debug/', views_debug.sessionsAndUsers, name="views_debug")
    ##path('views_debug/', views_debug.ApiHandler3, name="views_debug")

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('/__debug__/', include(debug_toolbar.urls)),
