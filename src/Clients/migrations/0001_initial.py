# Generated by Django 3.1.1 on 2020-09-30 05:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('doc_identification', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: +999999999. Up to 15 digits allowed.', regex='\\+?1?\\d{9,15}$')])),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_sender', models.CharField(max_length=30)),
                ('destination_address', models.CharField(max_length=30)),
                ('date_received', models.DateTimeField(auto_now_add=True)),
                ('state_package', models.CharField(choices=[('In_Warehouse', 'Warehouse'), ('In_Transit', 'Tranist'), ('Delivered', 'Delivered')], default='In_Warehouse', max_length=20)),
            ],
            options={
                'verbose_name': 'Package',
                'verbose_name_plural': 'Packages',
                'ordering': ['date_received'],
            },
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_guide', models.CharField(max_length=8)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('ubication', models.CharField(blank=True, max_length=30)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients.client')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients.package')),
            ],
            options={
                'verbose_name': 'Administrator',
                'verbose_name_plural': 'Administrators',
                'ordering': ['creation_date'],
            },
        ),
    ]
