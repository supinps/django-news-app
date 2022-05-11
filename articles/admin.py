from django.contrib import admin
from .models import Category, SubCategory, Article
# Register your models here.
class SubCategoryAdmin (admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['category']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'subcategory', 'created_at', 'is_approved']
    list_filter =['is_approved', 'subcategory', 'created_at', 'author']

admin.site.register(Category)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
