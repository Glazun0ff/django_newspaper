import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Article(models.Model):
    """Статьи"""
    article_title = models.CharField(verbose_name='заголовок', max_length=200)
    article_text = models.TextField(verbose_name='текст')
    created_at = models.DateTimeField(verbose_name='опубликовано', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='обновлено', auto_now=True)
    photo = models.ImageField(verbose_name='фото', upload_to='photos/%Y/%m/%d/', blank=True)
    category = models.ForeignKey('Category', verbose_name='категория', on_delete=models.PROTECT, null=True)
    views = models.IntegerField(verbose_name='кол-во просмотров', default=0)
    published = models.BooleanField(verbose_name='опубликовано', default=True)
    slug = models.SlugField(verbose_name='url', max_length=200, unique=True)

    def __str__(self):
        return self.article_title

    # def was_published_recently(self):
    #     return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def get_comment(self):
        return self.comments_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']


class Category(models.Model):
    """Категории"""
    title = models.CharField(verbose_name='название категория', max_length=150, db_index=True)
    slug = models.SlugField(verbose_name='url', max_length=150, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Comments(models.Model):
    """Комментарии"""
    name = models.CharField(verbose_name='имя', max_length=100)
    email = models.EmailField()
    text = models.CharField(verbose_name='комментарий', max_length=5000)
    datetime = models.DateTimeField(verbose_name='дата', auto_now_add=True)
    article = models.ForeignKey(Article, verbose_name='статья', on_delete=models.CASCADE)
    # parent = models.ForeignKey('self', verbose_name="родитель", on_delete=models.SET_NULL, blank=True, null=True)
    parent = models.ForeignKey('self', verbose_name="родитель", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.article}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
