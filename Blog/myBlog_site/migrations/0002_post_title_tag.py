# Generated by Django 4.2.6 on 2023-10-11 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My Blog', max_length=120),
        ),
    ]
