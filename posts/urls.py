from django.conf.urls import url #include importuje z pliku posts/urls.py
from django.contrib import admin

from . import views
#Jeżeli użyjesz from posts import view to w definicji funkcji
#nie musisz użyć "posts".


#Instrukacja jak tworzyć wyrażenie regularne dla linków:
# https://github.com/codingforentrepreneurs/Guides/blob/master/all/common_url_regex.md
urlpatterns = [
#   url(r'^admin/', admin.site.urls),
#   url(r'^posts/', app_name.views.function_name)
    url(r'^$', "posts.views.posts_list"),
    url(r'^create/$', "posts.views.posts_create"),
    url(r'^detail/$', "posts.views.posts_detail"),
    url(r'^update/$', "posts.views.posts_update"),
    url(r'^delete/$', "posts.views.posts_delete"),
]
