# Generated by Django 4.2.3 on 2023-10-17 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_article_like_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='like_users',
        ),
    ]
