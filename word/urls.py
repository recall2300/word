"""word URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from dangi import views

urlpatterns = [
    url(r'^$', views.main),
    url(r'^paper/$', views.show_test_paper, name='show_test_paper'),
    url(r'^create/$', views.create_voca, name='create_voca'),
    url(r'^admin/', views.admin),
    url(r'^admin2/', admin.site.urls),
]
