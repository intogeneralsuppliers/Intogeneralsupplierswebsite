# Generated by Django 3.0.7 on 2020-07-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sliderpic', '0002_slider_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='logo',
            field=models.ImageField(default='default.jpg', upload_to='slide_images'),
        ),
    ]
