# Generated by Django 4.0.5 on 2022-07-09 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_remove_cart_id_cart_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='uuid',
            new_name='id',
        ),
    ]
