# Generated by Django 4.0.2 on 2022-03-01 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0010_alter_order_computercode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.CharField(default='', max_length=50),
        ),
    ]