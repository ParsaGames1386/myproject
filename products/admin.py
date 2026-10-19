
from django.contrib import admin
from .models import Category, Product, File


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'parent',
        'is_enable',
        'created_time',
        'update_time',
    )

    search_fields = ('title', 'description')

    list_filter = (
        'is_enable',
        'parent',
        'created_time',
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'is_enable',
        'created_time',
        'update_time',
    )
    filter_horizontal = ('categories',)

    search_fields = ('title', 'description')

    list_filter = (
        'is_enable',
        'categories',
        'created_time',
    )


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'product',
        'created_time',
        'update_time',
    )

    search_fields = ('title', 'product__title')

    list_filter = ('created_time',)

class FileInlineAdmin(admin.StackedInline):
    model = File
    fields = ('title',"file_type",'file',"is_enable")
    extra = 0
