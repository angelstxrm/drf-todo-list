from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField('О себе', max_length=500, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'


class Complexity(models.Model):
    ComplexityTask = models.CharField('Сложность', max_length=11, default='Easy')

    def __str__(self):
        return self.ComplexityTask
    
    class Meta:
        verbose_name = 'Сложность'
        verbose_name_plural = 'Сложности'


class Status(models.Model):
    StatusTask = models.CharField('Статус', max_length=11, default='In progress')

    def __str__(self):
        return self.StatusTask
    
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Task(models.Model):
    title = models.CharField('Задача', max_length=100)
    description = models.TextField('Описание задачи', max_length=500, blank=True)
    complexity_bunch = models.ForeignKey(Complexity, verbose_name='Сложность', on_delete=models.CASCADE, blank=True, null=True, related_name='complexity')
    status_bunch = models.ForeignKey(Status, verbose_name='Статус', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    is_active = models.BooleanField('Активность', default=True)
    author = models.ForeignKey(CustomUser, verbose_name='Автор', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задачу'
        verbose_name_plural = 'Задачи'

