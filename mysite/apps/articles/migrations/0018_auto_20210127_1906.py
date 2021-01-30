# Generated by Django 3.1.5 on 2021-01-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0017_auto_20210125_1911'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2021-01-26 00:00', verbose_name='опубликовано'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='обновлено'),
        ),
    ]