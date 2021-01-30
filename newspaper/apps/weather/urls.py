from django.urls import path
from . import views

app_name = 'weather'
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>/', views.del_city),
]