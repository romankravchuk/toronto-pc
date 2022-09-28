# Generated by Django 4.1.1 on 2022-09-28 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("toronto", "0004_alter_customuser_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="component",
            name="price",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=8, verbose_name="price"
            ),
        ),
        migrations.AlterField(
            model_name="component",
            name="is_avaiable",
            field=models.BooleanField(default=False, verbose_name="is avaiable"),
        ),
    ]