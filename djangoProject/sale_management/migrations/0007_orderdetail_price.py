# Generated by Django 4.0.4 on 2022-05-06 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale_management', '0006_customer_created_at_customer_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
