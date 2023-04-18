"""
URL configuration for optimuspy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accounts/login/', views.LogIn.as_view(), name='login'),
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),
    path('accounts/logout/', views.ulogout, name='logout'),
    path('list/', views.ulist, name='list'),
    path('submit/', views.submit, name='submit')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
