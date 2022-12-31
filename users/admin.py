from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email','full_name']


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['user', 'caption', 'image', 'likes']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo', 'text']

class HashtagAdmin(admin.ModelAdmin):
    list_display = ['hashtag', 'photo']

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'action_user', 'action', 'photo']


admin.site.register(User, UserAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Hashtag, HashtagAdmin)
admin.site.register(Notification, NotificationAdmin)
