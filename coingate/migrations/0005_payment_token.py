# Generated by Django 3.0.3 on 2020-02-07 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coingate', '0004_auto_20200207_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='token',
            field=models.CharField(default=234, max_length=100),
            preserve_default=False,
        ),
    ]