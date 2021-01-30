from django import template
from django.db.models import Count, Sum
from django.utils import timezone
from articles.models import Article, Category, Comments

register = template.Library()


@register.simple_tag()
def get_categories():
    """Вывод всех категорий"""
    categories = Category.objects.annotate(cnt=Count('article')).filter(cnt__gt=0)
    return categories
    # return Category.objects.all()


@register.inclusion_tag('articles/tags/popular_articles.html')
def get_popular_articles(count=4):
    today = timezone.now()
    yesterday = today - timezone.timedelta(days=7)
    # popular_articles = Article.objects.filter(created_at__range=[yesterday, today]).order_by('-views')[:count]
    popular_articles = Article.objects.annotate(number_comments=Count('comments__article_id')).filter(
        created_at__range=[yesterday, today]).order_by('-views')[:count]
    return {'popular_articles': popular_articles}


@register.inclusion_tag('articles/tags/discussed_articles.html')
def get_discussed_articles(count=4):
    # discussed_articles = Article.objects.raw('SELECT *, Count(c.article_id) AS number_comments '
    #                                          'FROM articles_article a LEFT JOIN articles_comments c '
    #                                          'ON a.id = c.article_id '
    #                                          'GROUP BY a.id '
    #                                          'ORDER BY number_comments DESC, a.views DESC')[:count]
    today = timezone.now()
    yesterday = today - timezone.timedelta(days=7)
    discussed_articles = Article.objects.annotate(number_comments=Count('comments__article_id')).filter(
        created_at__range=[yesterday, today]).order_by('-number_comments', '-views')[:count]
    return {'discussed_articles': discussed_articles}

# @register.simple_tag()
# def get_categories_count():
#     categories = Category.objects.annotate(cnt=Count('article')).filter(cnt__gt=0)
#     for category in categories:
#         print(category.title, category.slug, category.cnt)
#
#
# @register.simple_tag()
# def get_popular_categories():
#     categories = Category.objects.annotate(sum_views=Sum('article__views'))
#     for category in categories:
#         print(category.title, category.sum_views)
#
# articles = Article.objects.values('article_title', 'comments__article')
# for a in articles:
#     print(a['article_title'], Count(a['comments__article']))
#
# Article.objects.raw('SELECT * FROM articles_article WHERE article_title = %s', ['текст заголовка'])
