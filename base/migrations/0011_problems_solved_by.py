# Generated by Django 4.0.6 on 2023-08-24 10:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0010_delete_equation_problems_user_delete_my_equa'),
    ]

    operations = [
        migrations.AddField(
            model_name='problems',
            name='solved_by',
            field=models.ManyToManyField(blank=True, related_name='solved_problems', to=settings.AUTH_USER_MODEL),
        ),
    ]
