# Generated by Django 3.0.7 on 2020-07-25 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Into_General_Suppliers', '0008_auto_20200725_0003'),
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_client', models.TextField(default='Costumer', max_length=1000)),
            ],
        ),
    ]