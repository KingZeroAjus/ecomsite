# Generated by Django 4.1.1 on 2022-10-12 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default='1', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.CharField(max_length=5000),
        ),
    ]
