# Generated by Django 4.2.2 on 2023-07-25 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_alter_product_reorder_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qps',
            field=models.IntegerField(blank=True, default='0'),
        ),
        migrations.AddField(
            model_name='product',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='total_quantity_sold',
            field=models.IntegerField(blank=True, default='0'),
        ),
        migrations.AddField(
            model_name='product',
            name='total_stock_sold',
            field=models.IntegerField(blank=True, default='0'),
        ),
        migrations.AlterField(
            model_name='product',
            name='reorder_level',
            field=models.IntegerField(blank=True, choices=[(5, 5), (4, 4), (3, 3), (2, 2), (1, 1)], default='2', null=True),
        ),
    ]