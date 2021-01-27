from django.core.exceptions import ValidationError
from django.db import models


class News(models.Model):
    """Новость"""
    title = models.CharField(max_length=150, verbose_name='Название новости')
    content = models.TextField(verbose_name='Текст новости')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title


class NewsComment(models.Model):
    """Комментарий"""
    MAX_COMMENT_LEVEL = 5

    text = models.TextField(verbose_name='Текст комментария', max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата опубликования комментария')
    owner = models.ForeignKey('profiles.User', verbose_name='Владелец комментария', on_delete=models.CASCADE, null=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Родитель', blank=True, null=True,
                               related_name='children')

    @property
    def level(self):
        child = self
        level = 0
        for i in range(0, self.MAX_COMMENT_LEVEL + 1):
            if child.parent:
                child = child.parent
                level += 1
        return level

    level.fget.short_description = 'Уровень вложенности комментария'

    def clean(self):
        child = self
        level = 0
        for i in range(0, self.MAX_COMMENT_LEVEL + 1):
            if child.parent:
                child = child.parent
                level += 1
            if level > self.MAX_COMMENT_LEVEL:
                raise ValidationError('Достигнут максимальный уровень вложенности')

    def __str__(self):
        if len(self.text) > 30:
            return self.text[:30] + '...'
        return self.text
