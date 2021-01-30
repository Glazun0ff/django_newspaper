from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.urls import reverse
from django.db.models import F
from django.core.mail import send_mail
from django.contrib import messages

from .models import Article, Category, Comments
from .forms import CommentForm


def index(request):
    return render(request, 'base.html')


# def list(request):
#     latest_articles_list = Article.objects.order_by('-pub_date')[:2]
#     return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})
#
#
# def detail(request, article_id):
#     try:
#         a = Article.objects.get(id=article_id)
#     except:
#         raise Http404('Статья не найдена!')
#     latest_comments_list = a.comment_set.order_by('-id')[:10]
#     return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})


class ArticlesList(ListView):
    """Список статей"""
    model = Article
    queryset = Article.objects.filter(published=True)
    paginate_by = 6


class ArticleDetail(DetailView):
    """Детализация статьи"""
    model = Article
    queryset = Article.objects.filter(published=True)
    # slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        # кол-во просмотров
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class ArticlesByCategory(ListView):
    """Статьи по категориям"""
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['article_title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


# def leave_comment(request, article_id):
#     try:
#         a = Article.objects.get(id=article_id)
#     except:
#         raise Http404('Статья не найдена!')
#     a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])
#     return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))


class AddComment(View):
    """Комментарии"""

    def post(self, request, pk):
        form = CommentForm(request.POST)
        article = Article.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.article = article
            form.save()
        return redirect(article.get_absolute_url())
        # return HttpResponseRedirect(reverse())


class Search(ListView):
    """Поиск статей"""
    paginate_by = 4

    def get_queryset(self):
        return Article.objects.filter(article_title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['s'] = f's={self.request.GET.get("s")}&'
        return context


def message(request):
    """Отправка сообщения"""
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        send_mail('Subject', message, 'no-reply@app.com', [email], fail_silently=False)
        # return HttpResponse("Письмо успешно отправлено на " + email)
        messages.add_message(request, messages.INFO, 'Письмо успешно отправлено на ' + email)
    return render(request, 'message.html')
