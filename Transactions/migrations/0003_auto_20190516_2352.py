# Generated by Django 2.2.1 on 2019-05-16 23:52

import creditcards.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Transactions', '0002_auto_20190515_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc_number', creditcards.models.CardNumberField(max_length=25, verbose_name='card number')),
                ('cc_expiry', creditcards.models.CardExpiryField(verbose_name='expiration date')),
                ('cc_code', creditcards.models.SecurityCodeField(max_length=4, verbose_name='security code')),
            ],
        ),
        migrations.AddField(
            model_name='transactions',
            name='credit_card',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Transactions.CreditCard'),
            preserve_default=False,
        ),
    ]
