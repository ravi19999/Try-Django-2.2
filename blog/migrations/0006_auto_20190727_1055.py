# Generated by Django 2.2 on 2019-07-27 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190725_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='text',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='content',
            field=models.TextField(default='someone'),
            preserve_default=False,
        ),
    ]
