# Generated by Django 4.0.6 on 2023-08-15 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_problems_area_in_remove_problems_x_intercept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='solution_x',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='problems',
            name='solution_y',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]