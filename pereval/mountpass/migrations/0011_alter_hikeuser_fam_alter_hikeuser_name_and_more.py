# Generated by Django 4.2.15 on 2024-08-20 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mountpass', '0010_alter_hikeuser_fam_alter_hikeuser_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hikeuser',
            name='fam',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='hikeuser',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='hikeuser',
            name='otc',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='hikeuser',
            name='phone',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
