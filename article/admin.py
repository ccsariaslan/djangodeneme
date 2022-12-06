from django.contrib import admin

from .models import article,Comment

# Register your models here.
@admin.register(Comment)
class articleComments(admin.ModelAdmin):
    list_display = ['commentarea','commentauthor','commentdate']
    class Meta():
        model = Comment
        
 
    

@admin.register(article)
class articleadmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    list_display_links = ["title","created_date"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    class Meta():
        model = article
        