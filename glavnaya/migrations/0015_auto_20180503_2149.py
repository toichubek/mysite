# Generated by Django 2.0.4 on 2018-05-03 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glavnaya', '0014_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='urlname',
            field=models.TextField(blank=True, help_text='не обязательно', null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='url',
            field=models.URLField(blank=True, help_text='не обязательно', null=True),
        ),
    ]
