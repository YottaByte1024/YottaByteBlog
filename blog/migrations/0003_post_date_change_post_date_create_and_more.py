# Generated by Django 4.1.2 on 2022-10-16 15:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_abstract'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_change',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='abstract',
            field=models.TextField(default='', max_length=500),
        ),
    ]
