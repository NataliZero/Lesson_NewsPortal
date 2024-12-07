from django.shortcuts import render
from .models import News

def news_list(request):
    news = News.objects.all()  # Получаем все новости из базы данных
    return render(request, 'news/news_list.html', {'news': news})  # Передаём новости в шаблон
