from django.conf.urls import url, include 
#from django.contrib.auth import views as auth_views 
#from django.contrib.auth import   logout #authenticate,login,
#from auth_views import login, logout
from django.contrib.auth import authenticate, login, logout

urlpatterns = [ 
    url(r'^', include('tutorials.urls')),
 
]   