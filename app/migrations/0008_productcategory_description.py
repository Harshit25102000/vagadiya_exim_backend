# Generated by Django 4.2.13 on 2024-07-11 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_productpagedetails_related_products_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
