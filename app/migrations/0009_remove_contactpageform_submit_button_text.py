# Generated by Django 4.2.13 on 2024-07-11 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_productcategory_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactpageform',
            name='submit_button_text',
        ),
    ]