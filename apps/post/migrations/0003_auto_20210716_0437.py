# Generated by Django 3.2.5 on 2021-07-15 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(default='post/category/default.png', upload_to='post/category/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=64, null=True, unique=True),
        ),
    ]
