# Generated by Django 4.1.5 on 2023-01-18 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='appointed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='from_time',
            field=models.CharField(blank=True, choices=[('06:00', '07:00'), ('08:00', '09:00'), ('10:00', '11:00'), ('13:00', '14:00'), ('15:00', '16:00')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='to_time',
            field=models.CharField(blank=True, choices=[('06:00', '07:00'), ('08:00', '09:00'), ('10:00', '11:00'), ('13:00', '14:00'), ('15:00', '16:00')], max_length=30, null=True),
        ),
    ]
