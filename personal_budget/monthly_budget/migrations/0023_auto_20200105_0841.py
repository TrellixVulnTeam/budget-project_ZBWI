# Generated by Django 2.2.6 on 2020-01-05 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monthly_budget', '0022_auto_20200105_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_code',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=False,
        ),
    ]
