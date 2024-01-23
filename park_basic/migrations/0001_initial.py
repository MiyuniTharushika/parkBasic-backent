# Generated by Django 5.0.1 on 2024-01-22 13:08

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='bookingSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slotName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='bookingTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookingTime', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='reserver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carNo', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Enter a valid car registration number.', regex='^([a-zA-Z]{1,3}|([0-9]{1,3}))-[0-9]{4}$')])),
                ('phnNo', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Enter a valid Sri Lankan phone number.', regex='^(?:7|0|(?:\\+94))[0-9]{9,10}$')])),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('slotId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='park_basic.bookingslot')),
                ('timeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='park_basic.bookingtime')),
                ('reserverId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='park_basic.reserver')),
            ],
        ),
    ]