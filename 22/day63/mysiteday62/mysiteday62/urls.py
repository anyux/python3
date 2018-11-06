"""mysiteday62 URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    # 出版社
    url(r'^admin/', admin.site.urls),
    url(r'^pub_list/', views.pub_list),
    url(r'^pub_add/', views.pub_add),
    url(r'^pub_del/', views.pub_del),
    url(r'^pub_edit/', views.pub_edit),

    # 书
    url(r'^book_list/', views.book_list),
    url(r'^book_add/', views.book_add),
]
