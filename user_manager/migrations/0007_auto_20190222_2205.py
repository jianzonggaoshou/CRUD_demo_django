# Generated by Django 2.0.6 on 2019-02-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0006_auto_20190222_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownuser',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]