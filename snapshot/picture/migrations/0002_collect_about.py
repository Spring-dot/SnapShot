# Generated by Django 2.2 on 2020-06-11 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collect',
            name='about',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]