# Generated by Django 4.2.15 on 2024-08-21 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mountpass', '0013_alter_pereval_add_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pereval',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
