from django.contrib import admin

# Register your models here.
from main.models import Book, Order


admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'year')
    search_fields = ('author', 'title')
    ordering = ('author', )
admin.site.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'days_count', 'date')
    filter_horizontal = ('books', )
    readonly_fields = ('date', )
