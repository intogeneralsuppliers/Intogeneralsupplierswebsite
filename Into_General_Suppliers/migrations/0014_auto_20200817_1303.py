# Generated by Django 3.0.7 on 2020-08-17 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Into_General_Suppliers', '0013_auto_20200817_1242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service_card',
            old_name='blumbing',
            new_name='building',
        ),
        migrations.RenameField(
            model_name='service_card',
            old_name='blumbing_content',
            new_name='building_content',
        ),
    ]