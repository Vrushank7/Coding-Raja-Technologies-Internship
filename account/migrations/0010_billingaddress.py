# Generated by Django 3.2.4 on 2021-06-24 07:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20210620_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{0,9}$')])),
                ('pin_code', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^\\d{0,9}$')])),
                ('house_no', models.CharField(max_length=300)),
                ('landmark', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
            ],
        ),
    ]