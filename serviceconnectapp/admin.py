from django.contrib import admin
from .models import Showcase, Category, Service, Review

@admin.register(Showcase)
class ShowcaseAdmin(admin.ModelAdmin):
    list_display = ('show_name', 'show_txt', 'show_img')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','cat_name','cat_image']
    list_editable = ['cat_name','cat_image']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id','category_id','category','name', 'description', 'image', 'phone', 'address', 'city', 'state', 'zip_code', 'website','special','domestic', 'tech', 'events', 'catering', 'hair', 'automobile', 'beauty', 'more']
    list_editable = ['category', 'name', 'image', 'description', 'phone','address', 'city', 'state', 'zip_code', 'website','special','domestic', 'tech', 'events', 'catering', 'hair', 'automobile', 'beauty', 'more']

@admin.register(Review)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['service', 'user', 'comment', 'created_at']