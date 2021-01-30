from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Article, Category, Comments


class ArticleAdminForm(forms.ModelForm):
    article_text = forms.CharField(label='Текст статьи', widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'


class CommentInline(admin.StackedInline):
    """Комментарии на странице статьи"""
    model = Comments
    extra = 1
    readonly_fields = ("name", "email")


@admin.register(Article)
class ArticlesAdmin(admin.ModelAdmin):
    """Статьи"""
    prepopulated_fields = {'slug': ('article_title',)}  # slug
    list_display = ('id', 'created_at', 'updated_at', 'article_title', 'category', 'get_photo', 'views', 'published')
    list_display_links = ('created_at', 'article_title')
    search_fields = ('article_title',)
    list_editable = ('published',)
    list_filter = ('published', 'category')
    form = ArticleAdminForm
    fields = ('article_title', 'slug', 'category', 'article_text', 'photo', 'get_photo', 'created_at', 'updated_at', 'views', 'published')
    readonly_fields = ('get_photo', 'created_at', 'updated_at', 'views',)
    inlines = [CommentInline]

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = "Изображение"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}  # slug
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    fields = ('title', 'slug')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    """Комментарии"""
    list_display = ('id', 'datetime', 'name', 'email', 'short_text', 'parent', 'article')
    fields = ('name', 'email', 'datetime', 'text', 'parent', 'article')
    readonly_fields = ('name', 'email', 'datetime')
    list_display_links = ('datetime', 'name', 'email')
    list_filter = ('name', 'datetime')
    search_fields = ('article__article_title',)  # поиск article_title по ForeignKey article

    @staticmethod
    def short_text(self):
        return self.text if len(self.text) < 101 else (self.text[:100] + '...')


# admin.site.register(Article, ArticleAdmin)
# admin.site.register(Comment)


admin.site.site_title = "Django News"
admin.site.site_header = "Django News"
# admin.site.index_title = 'Django News'
