"""trydjango19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url #include importuje z pliku posts/urls.py
from django.contrib import admin

#Jeżeli użyjesz from posts import view to w definicji funkcji
#nie musisz użyć "posts".


#Instrukacja jak tworzyć wyrażenie regularne dla linków:
# https://github.com/codingforentrepreneurs/Guides/blob/master/all/common_url_regex.md
urlpatterns = [
    url(r'^admin/', admin.site.urls),
#   url(r'^posts/', app_name.views.function_name)
    url(r'^posts/', include("posts.urls")),
]
