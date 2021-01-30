from django.urls import path

from .views import *

# app_name = 'articles'
urlpatterns = [
    # path('', index, name='index'),
    path('', ArticlesList.as_view()),
    path('<slug:slug>', ArticleDetail.as_view(), name='article_detail'),
    path('category/<slug:slug>/', ArticlesByCategory.as_view(), name='category'),
    path('comment/<int:pk>/', AddComment.as_view(), name='add_comment'),
    # path('articles/', views.list, name='list'),
    # path('articles/<int:article_id>/', views.detail, name='detail'),
    # path('articles/<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    path('search/', Search.as_view(), name='search'),
    path('message/', message, name='message'),
]