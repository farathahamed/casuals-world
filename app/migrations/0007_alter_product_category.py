# Generated by Django 4.2.3 on 2023-08-21 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CHCT', 'casual half sleeve coller Tshirt'), ('CFRT', 'casual full sleeve round neck Tshirt'), ('CHRT', 'casual half sleeve round neck Tshirt'), ('CH', 'casual half hand shirt'), ('JN', 'jeans'), ('CF', 'casual full hand shirt')], max_length=4),
        ),
    ]