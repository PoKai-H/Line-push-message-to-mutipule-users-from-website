from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('', views.showtemplate),
    path('create',views.Message_create_view),
    path('create/send',views.MessagePush),
    path('create/test',views.MessageCreateTest_Create),
    path('create/test/send',views.MessageCreateTest_Send),
]