from django.contrib import admin
from authentication.models import Profile
from .models import Post, Like, Comment

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'location', 'photo']
    raw_id_fields = ['user']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['content', 'created_at']
    raw_id_fields = ['user']
    
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post']
    raw_id_fields = ['user']
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'content', 'created_at']
    raw_id_fields = ['user']