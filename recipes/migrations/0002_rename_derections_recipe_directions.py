# Generated by Django 5.1.3 on 2025-01-20 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='derections',
            new_name='directions',
        ),
    ]
