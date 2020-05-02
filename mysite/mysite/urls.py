"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views# Becuase we want only superusers to Login or Logout
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('blog.urls')),#include all urls of the Application 'blog'
    url(r'account/login/$',views.login,name='login'), #here basically whats happening is that we are only allowin superusers to login and Logout!
    url(r'account/logout/$',views.logout,name='logout',kwargs={'next_page':'/'}), # kwargs or Key word arguments are used here so that after logging out we are redirected to '/' which is nothing but our HomePage i.r our post_list page!
]
