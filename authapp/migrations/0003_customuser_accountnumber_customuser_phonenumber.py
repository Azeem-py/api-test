# Generated by Django 4.0.3 on 2022-06-26 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_remove_customuser_accountnumber_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='accountNumber',
            field=models.IntegerField(default=8393935358),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='phoneNumber',
            field=models.IntegerField(default=589792749, unique=True),
            preserve_default=False,
        ),
    ]
