# Generated by Django 2.2.6 on 2020-01-04 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monthly_budget', '0018_auto_20200104_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planned_sum', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='monthly_budget.Category')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='monthly_budget.Period')),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='chained_transaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='monthly_budget.Transaction'),
        ),
        migrations.DeleteModel(
            name='Budget',
        ),
    ]