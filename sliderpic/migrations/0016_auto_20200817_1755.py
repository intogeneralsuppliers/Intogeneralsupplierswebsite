# Generated by Django 3.0.7 on 2020-08-17 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sliderpic', '0015_auto_20200817_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flooring',
            old_name='flooring',
            new_name='flooring2',
        ),
        migrations.AddField(
            model_name='flooring',
            name='flooring3',
            field=models.ImageField(default='default.jpg', upload_to='flooring_images'),
        ),
        migrations.AddField(
            model_name='flooring',
            name='flooring4',
            field=models.ImageField(default='default.jpg', upload_to='flooring_images'),
        ),
        migrations.AddField(
            model_name='flooring',
            name='flooring5',
            field=models.ImageField(default='default.jpg', upload_to='flooring_images'),
        ),
    ]
