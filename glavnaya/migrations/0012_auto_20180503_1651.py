# Generated by Django 2.0.4 on 2018-05-03 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glavnaya', '0011_auto_20180503_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
    ]
