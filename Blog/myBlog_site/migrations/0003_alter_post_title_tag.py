# Generated by Django 4.2.6 on 2023-10-11 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog_site', '0002_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(max_length=120),
        ),
    ]
