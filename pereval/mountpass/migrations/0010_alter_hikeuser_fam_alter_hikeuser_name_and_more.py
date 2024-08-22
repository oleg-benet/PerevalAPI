# Generated by Django 4.2.15 on 2024-08-20 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mountpass', '0009_image_date_added_alter_image_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hikeuser',
            name='fam',
            field=models.CharField(blank=True, max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='hikeuser',
            name='name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='hikeuser',
            name='otc',
            field=models.CharField(blank=True, max_length=50, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='hikeuser',
            name='phone',
            field=models.CharField(blank=True, max_length=50, verbose_name='Телефон'),
        ),
    ]
