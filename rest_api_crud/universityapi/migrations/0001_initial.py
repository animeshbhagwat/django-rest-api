# Generated by Django 3.0.8 on 2020-07-26 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Univeristy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alpha_two_code', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('domain', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('web_page', models.CharField(max_length=100)),
            ],
        ),
    ]