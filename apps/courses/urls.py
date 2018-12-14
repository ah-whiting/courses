from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.root),
    url(r'^courses/create', views.create_course),
    url(r'^courses/delete/(?P<id>\d+)', views.delete_course),
]