# Generated by Django 4.2.6 on 2023-10-16 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog_site', '0007_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click link above to read blog post....', max_length=120),
        ),
    ]