from django.db import models
from django.contrib import admin
# Create your models here.

class Group(models.Model):
    group = models.CharField(max_length=100)
    def __str__(self):
        return self.group
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id','group']
    list_filter = ['group']
    search_fields = ['group']

class UserID(models.Model):
    group = models.ForeignKey(Group, on_delete= models.CASCADE)
    user_id = models.CharField(max_length=100)
    def __str__(self):
        return self.user_id

@admin.register(UserID)
class UserIDAdmin(admin.ModelAdmin):
    list_display = ['group','user_id']
    list_filter = ['group']
    search_field = ['group']

class Message(models.Model):
    group = models.ForeignKey(Group, on_delete= models.CASCADE)
    message_title = models.CharField(max_length=100)
    message_push = models.CharField(max_length=200)
    def __str__(self):
        return self.message_push

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id','group','message_title']
    list_filter = ['id','group']
    search_fields = ['id','group','message_title']

class Test(models.Model):
    user_id = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    def __str__(self) :
        return self.text

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['user_id','text']