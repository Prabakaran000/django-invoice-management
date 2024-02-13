# Generated by Django 4.1.13 on 2024-02-07 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('S_No', models.AutoField(primary_key=True, serialize=False)),
                ('consignment_No', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('weight', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
            ],
        ),
    ]
