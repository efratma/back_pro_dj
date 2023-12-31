# Generated by Django 4.0.6 on 2023-08-29 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_solvedexercise_delete_userhits'),
    ]

    operations = [
        migrations.AddField(
            model_name='solvedexercise',
            name='context',
            field=models.CharField(choices=[('QUIZ', 'Quiz'), ('TEST', 'Test')], default='QUIZ', max_length=50),
        ),
        migrations.AddField(
            model_name='solvedexercise',
            name='exercise_type',
            field=models.CharField(default='CUTTING_POINTS', max_length=50),
        ),
        migrations.AddField(
            model_name='solvedexercise',
            name='number_solved',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
