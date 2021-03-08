from django.contrib import admin
from .models import *
 
# Register your models here.

class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('courses', 'title', 'slug', 'created_on')
    list_filter = ['courses']
    fieldsets = (
        ("Title", {
            'fields': ['title', 'created_by']
        }),
        ('Content', {
            'fields': [ 'content']
        }),
         ('Connect connect page to course', {
            'fields': ['courses']
        }),
        ('Slug: No need to edit', {
            'fields': ['slug']
        }),
    )
    search_fields = ['title', 'content', 'created_on']
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('parent_discussion', 'created_by', 'content', 'created_on')
    list_filter = ['created_on']
    fieldsets = (
        ("Parent Discussion", {
            'fields': ['parent_discussion']
        }),
        ('Author', {
            'fields': ['created_by']
        }),
        ('Comment Content', {
            'fields': ['content']
        }),
    )
    search_fields = ('created_by', 'content', 'created_on')

admin.site.register(Discussion, DiscussionAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply)