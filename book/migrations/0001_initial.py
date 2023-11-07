# Generated by Django 4.1.5 on 2023-01-18 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=30)),
                ('appointed_date', models.DateField()),
                ('from_time', models.CharField(choices=[('06:00', '07:00'), ('08:00', '09:00'), ('10:00', '11:00'), ('13:00', '14:00'), ('15:00', '16:00')], max_length=30)),
                ('to_time', models.CharField(choices=[('06:00', '07:00'), ('08:00', '09:00'), ('10:00', '11:00'), ('13:00', '14:00'), ('15:00', '16:00')], max_length=30)),
                ('order_number', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]