# Generated by Django 2.2.12 on 2020-06-11 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('start_end', models.DateTimeField(blank=True, null=True)),
                ('degree', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
            ],
        ),
    ]
