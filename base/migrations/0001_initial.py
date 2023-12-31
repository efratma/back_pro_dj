# Generated by Django 4.0.6 on 2023-08-08 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equa_name', models.CharField(blank=True, max_length=50, null=True)),
                ('desc_equa', models.CharField(blank=True, max_length=50, null=True)),
                ('grade', models.DecimalField(decimal_places=2, max_digits=5)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='problems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line1_equation', models.CharField(max_length=255, null=True)),
                ('line2_equation', models.CharField(max_length=255, null=True)),
                ('intersection_point', models.CharField(max_length=255, null=True)),
                ('line_equation', models.CharField(max_length=255)),
                ('x_intercept', models.IntegerField(null=True)),
                ('area_in', models.IntegerField(null=True)),
                ('base', models.FloatField(null=True)),
                ('height', models.FloatField(null=True)),
                ('area', models.FloatField(null=True)),
                ('point1_x', models.IntegerField(default=0)),
                ('point1_y', models.IntegerField(default=0)),
                ('point2_x', models.IntegerField(default=0)),
                ('point2_y', models.IntegerField(default=0)),
                ('slope', models.IntegerField(default=0)),
                ('y_intercept', models.IntegerField(default=0)),
                ('equation', models.CharField(default='', max_length=100)),
                ('a_fl', models.FloatField(null=True)),
                ('b_fl', models.FloatField(null=True)),
                ('c_fl', models.FloatField(null=True)),
                ('option', models.CharField(max_length=1)),
                ('result', models.IntegerField(null=True)),
                ('correct_answer_fl', models.FloatField(blank=True, null=True)),
                ('equation_text', models.CharField(default='Default Equation', max_length=255)),
                ('correct_answer', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('a', models.IntegerField(default=0)),
                ('b', models.IntegerField(default=0)),
                ('c', models.IntegerField(default=0)),
                ('d', models.IntegerField(default=0)),
                ('e', models.IntegerField(default=0)),
                ('f', models.IntegerField(default=0)),
                ('g', models.IntegerField(default=0)),
                ('solution_x', models.FloatField(default=0.0)),
                ('solution_y', models.FloatField(default=0.0)),
                ('equation1', models.CharField(max_length=255)),
                ('equation2', models.CharField(max_length=255)),
                ('problem_str', models.TextField(null=True)),
                ('solution', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='my_equa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equation', models.CharField(blank=True, max_length=50, null=True)),
                ('equa_name', models.CharField(blank=True, max_length=50, null=True)),
                ('is_correct', models.BooleanField(default=False)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
