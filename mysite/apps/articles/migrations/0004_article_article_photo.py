# Generated by Django 3.1.5 on 2021-01-16 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20210116_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_photo',
            field=models.ImageField(null=True, upload_to='articles/', verbose_name='фото статьи'),
        ),
    ]
