from django.contrib import admin  

from main.models import Comment, Comment1  

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin): 
    list_display = ('user', 'text', 'created_at')  
    ordering = ('-created_at',)  
    search_fields = ('text',)  

@admin.register(Comment1)
class Comment1Admin(admin.ModelAdmin): 
    list_display = ('user', 'text', 'created_at')  
    ordering = ('-created_at',)  
    search_fields = ('text',)  
