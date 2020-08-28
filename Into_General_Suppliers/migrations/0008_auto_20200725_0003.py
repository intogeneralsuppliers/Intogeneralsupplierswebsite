# Generated by Django 3.0.7 on 2020-07-24 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Into_General_Suppliers', '0007_auto_20200724_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_card',
            name='electricity_content',
            field=models.TextField(default='name', max_length=1000),
        ),
        migrations.AlterField(
            model_name='service_card',
            name='extentions_content',
            field=models.TextField(default='name', max_length=1000),
        ),
        migrations.AlterField(
            model_name='service_card',
            name='flooring_content',
            field=models.TextField(default='name', max_length=1000),
        ),
        migrations.AlterField(
            model_name='service_card',
            name='painting_content',
            field=models.TextField(default='name', max_length=1000),
        ),
        migrations.AlterField(
            model_name='service_card',
            name='paving_content',
            field=models.TextField(default='name', max_length=1000),
        ),
        migrations.AlterField(
            model_name='service_card',
            name='plumbing_content',
            field=models.TextField(default='name', max_length=1000),
        ),
        migrations.AlterField(
            model_name='service_card',
            name='renovations_content',
            field=models.TextField(default='name', max_length=1000),
        ),
        migrations.AlterField(
            model_name='service_card',
            name='roofing_content',
            field=models.TextField(default='name', max_length=1000),
        ),
        migrations.AlterField(
            model_name='service_card',
            name='walling_content',
            field=models.TextField(default='name', max_length=1000),
        ),
    ]