# Generated by Django 2.2.6 on 2020-01-05 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monthly_budget', '0021_auto_20200105_0752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='balance',
            old_name='planned_sum',
            new_name='planned_amount',
        ),
    ]