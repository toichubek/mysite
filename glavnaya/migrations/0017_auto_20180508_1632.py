# Generated by Django 2.0.4 on 2018-05-08 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glavnaya', '0016_auto_20180507_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news/'),
        ),
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='team/'),
        ),
    ]
