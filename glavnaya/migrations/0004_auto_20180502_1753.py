# Generated by Django 2.0.4 on 2018-05-02 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glavnaya', '0003_remove_news_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='preview',
            field=models.TextField(default=models.TextField(), max_length=35),
        ),
        migrations.AlterField(
            model_name='news',
            name='FotoUrl',
            field=models.CharField(default='/static/', max_length=100),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
