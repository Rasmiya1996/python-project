# Generated by Django 5.0.3 on 2024-11-20 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product_app", "0002_remove_item_quantity_sold"),
    ]

    operations = [
        migrations.RenameField(
            model_name="paymoney",
            old_name="quantity",
            new_name="quantity_2",
        ),
    ]
