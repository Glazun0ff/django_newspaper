# Generated by Django 3.1.5 on 2021-01-28 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0018_auto_20210127_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.comments', verbose_name='родитель'),
        ),
    ]
