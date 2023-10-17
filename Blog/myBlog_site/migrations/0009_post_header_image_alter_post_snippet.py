# Generated by Django 4.2.6 on 2023-10-16 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog_site', '0008_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(max_length=120),
        ),
    ]