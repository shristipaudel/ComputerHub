# Generated by Django 4.0.2 on 2022-03-01 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0005_alter_computerspecification_price_max_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='computerspecification',
            name='computercode',
            field=models.IntegerField(default=0),
        ),
    ]
