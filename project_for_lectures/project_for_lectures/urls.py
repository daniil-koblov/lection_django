"""
URL configuration for project_for_lectures project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from lectureapp_3_1.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_menu_1_1/', include('lectureapp_1_1.urls')),
    path('main_menu_3_1/', include('lectureapp_3_1.urls')),
    path('', index, name='index'),
    path('main_menu_4_1/', include('lectureapp_4_1.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('main_menu_6_1/', include('lectureapp_6_1.urls')),
]
