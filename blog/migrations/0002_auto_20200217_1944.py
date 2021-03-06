# Generated by Django 3.0.3 on 2020-02-17 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='summary',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default='', max_length=250),
        ),
    ]
