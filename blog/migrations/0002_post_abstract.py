# Generated by Django 4.1.2 on 2022-10-15 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='abstract',
            field=models.TextField(default='', max_length=300),
        ),
    ]
