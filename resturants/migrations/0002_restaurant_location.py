# Generated by Django 2.0 on 2017-12-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='location',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
