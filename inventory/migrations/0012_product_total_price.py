# Generated by Django 4.2.2 on 2023-07-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_remove_product_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=40, max_digits=10),
            preserve_default=False,
        ),
    ]