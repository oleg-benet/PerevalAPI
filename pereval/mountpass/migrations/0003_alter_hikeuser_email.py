# Generated by Django 4.2.15 on 2024-08-16 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mountpass', '0002_alter_image_image_alter_image_pereval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hikeuser',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
