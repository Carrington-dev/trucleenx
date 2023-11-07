# Generated by Django 4.1.5 on 2023-01-18 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_order_appointed_date_alter_order_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='to_time',
        ),
        migrations.AlterField(
            model_name='order',
            name='from_time',
            field=models.CharField(blank=True, choices=[('06:00 am to 07.00 am', '06:00 am to 07.00 am'), ('07:00 am to 08:00 am', '07:00 am to 08:00 am'), ('08:00 am to 09:00 am', '08:00 am to 09:00 am'), ('09:00 am to 10:00 am', '09:00 am to 10:00 am'), ('10:00 am to 11:00 am', '10:00 am to 11:00 am'), ('11:00 am to 12:00 pm', '11:00 am to 12:00 pm'), ('12:00 pm to 01:00 pm', '12:00 pm to 01:00 pm'), ('01:00 pm to 02.00 pm', '01:00 pm to 02.00 pm'), ('02:00 pm to 03:00 pm', '02:00 pm to 03:00 pm'), ('03:00 pm to 04:00 pm', '03:00 pm to 04:00 pm'), ('04:00 pm to 05:00 pm', '04:00 pm to 05:00 pm'), ('05:00 pm to 06:00 pm', '05:00 pm to 06:00 pm')], max_length=30, null=True),
        ),
    ]