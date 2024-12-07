from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)  # Заголовок новости
    short_description = models.CharField(max_length=500)  # Краткое описание
    text = models.TextField()  # Полный текст
    pub_date = models.DateTimeField(auto_now_add=True)  # Дата публикации
    author = models.CharField(max_length=100)  # Автор новости

    def __str__(self):
        return self.title  # Отображение в панели администратора
