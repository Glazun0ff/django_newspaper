# Generated by Django 3.1.5 on 2021-01-18 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_remove_article_draft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
