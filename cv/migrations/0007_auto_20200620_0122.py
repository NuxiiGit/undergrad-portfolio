# Generated by Django 2.2.12 on 2020-06-20 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0006_auto_20200618_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
