# Generated by Django 4.0.6 on 2023-09-11 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0003_tokenproxy'),
        ('base', '0020_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='invalidated_tokens',
            field=models.ManyToManyField(blank=True, to='authtoken.token'),
        ),
    ]
