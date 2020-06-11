# Generated by Django 2.2.12 on 2020-06-11 19:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_qualification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=70)),
                ('phone', models.TextField(validators=[django.core.validators.RegexValidator('\\+([0-9]{1,15})')])),
            ],
        ),
        migrations.DeleteModel(
            name='Qualification',
        ),
    ]