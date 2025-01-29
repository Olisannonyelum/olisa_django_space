# Generated by Django 5.1.3 on 2025-01-25 14:43

import recipes.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_rename_derections_recipe_directions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(max_length=50, validators=[recipes.validators.validate_unit_of_measure]),
        ),
    ]
