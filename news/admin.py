from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author')  # Поля, отображаемые в списке
    search_fields = ('title', 'author')  # Поля для поиска
    list_filter = ('pub_date',)  # Фильтр по дате публикации
