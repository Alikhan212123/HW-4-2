from django.contrib import admin
from django.urls import path
from posts.views import hello,time  , goodbye
from django.http import HttpResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('time/', time),
    path('goodbye/', goodbye)

 ]
