# Generated by Django 2.2.12 on 2020-06-21 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0011_auto_20200620_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
