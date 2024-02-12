# Generated by Django 4.2.3 on 2023-08-23 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_cloth_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('CHRT', 'casual-half-sleeve-round-neck-Tshirts'), ('CFS', 'casual-full-size-shirts'), ('JN', 'jeans'), ('CFRT', 'casual-full-sleeve-round-neck-Tshirts'), ('CHCT', 'casual-half-sleeve-collar-Tshirts'), ('CHS', 'casual-half-size=shirts')], max_length=4)),
                ('dress_image', models.ImageField(upload_to='dress')),
            ],
        ),
        migrations.DeleteModel(
            name='Cloth',
        ),
    ]