# Generated by Django 2.2.6 on 2019-10-31 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20191031_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='value',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
