# Generated by Django 5.0.3 on 2024-03-25 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='Product',
            new_name='product',
        ),
    ]
