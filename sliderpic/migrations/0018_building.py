# Generated by Django 3.0.7 on 2020-08-17 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sliderpic', '0017_auto_20200817_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building1', models.ImageField(default='default.jpg', upload_to='building_images')),
                ('building2', models.ImageField(default='default.jpg', upload_to='building_images')),
                ('building3', models.ImageField(default='default.jpg', upload_to='building_images')),
                ('building4', models.ImageField(default='default.jpg', upload_to='building_images')),
                ('building5', models.ImageField(default='default.jpg', upload_to='building_images')),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
