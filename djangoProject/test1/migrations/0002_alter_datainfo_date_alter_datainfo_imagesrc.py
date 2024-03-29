# Generated by Django 4.1 on 2023-01-13 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test1", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datainfo",
            name="date",
            field=models.DateField(
                default="", max_length=30, unique=True, verbose_name="日期"
            ),
        ),
        migrations.AlterField(
            model_name="datainfo",
            name="imagesrc",
            field=models.CharField(default="", max_length=30, verbose_name="传感器类型"),
        ),
    ]
