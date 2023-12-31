# Generated by Django 4.2.6 on 2023-10-17 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog_site', '0010_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='printerest_url',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='website_url',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
