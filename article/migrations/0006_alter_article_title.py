# Generated by Django 5.1.3 on 2024-12-21 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
