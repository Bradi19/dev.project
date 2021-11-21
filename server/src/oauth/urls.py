from django.contrib import admin
from django.urls import path, include
from server.src.oauth.endpoint import views
from django.conf.urls import url
urlpatterns = [
        url(r'^api/customers/$', views.customers_list),
#       url(r'^api/customers/(?P<pk>[0-9]+)$', views.customers_detail),
]