# Generated by Django 5.1 on 2024-08-24 07:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_product_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
