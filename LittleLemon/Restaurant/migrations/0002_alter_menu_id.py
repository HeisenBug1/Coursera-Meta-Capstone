# Generated by Django 5.1 on 2024-09-24 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
