# Generated by Django 3.1.5 on 2021-01-25 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_auto_20210124_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default='1970-01-01 03:00', verbose_name='дата'),
            preserve_default=False,
        ),
    ]