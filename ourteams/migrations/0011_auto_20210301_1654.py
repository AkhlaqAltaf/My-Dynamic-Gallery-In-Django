# Generated by Django 3.1.3 on 2021-03-01 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourteams', '0010_auto_20210301_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourgallery',
            name='fb_url',
            field=models.CharField(blank=True, default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='ourgallery',
            name='insta_url',
            field=models.CharField(blank=True, default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='ourgallery',
            name='linkedn_url',
            field=models.CharField(blank=True, default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='ourgallery',
            name='twitter_url',
            field=models.CharField(blank=True, default='#', max_length=100),
        ),
    ]
