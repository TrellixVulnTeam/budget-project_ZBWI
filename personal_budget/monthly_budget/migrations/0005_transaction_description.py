# Generated by Django 2.2.6 on 2019-11-06 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monthly_budget', '0004_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
