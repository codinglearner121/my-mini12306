# Generated by Django 5.2.1 on 2025-05-26 02:54

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
            name='TrainTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_number', models.CharField(max_length=10, verbose_name='车次')),
                ('departure', models.CharField(max_length=50, verbose_name='出发地')),
                ('destination', models.CharField(max_length=50, verbose_name='目的地')),
                ('departure_time', models.DateTimeField(verbose_name='出发时间')),
                ('seat_type', models.CharField(choices=[('二等座', '二等座'), ('一等座', '一等座'), ('商务座', '商务座')], max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='票价')),
                ('available_seats', models.PositiveIntegerField(default=100, verbose_name='余票')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
