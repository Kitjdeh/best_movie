# Generated by Django 3.2.13 on 2022-11-24 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_like_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='title',
            field=models.CharField(max_length=20, null=True),
        ),
    ]