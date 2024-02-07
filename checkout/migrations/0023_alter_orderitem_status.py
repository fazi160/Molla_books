# Generated by Django 4.2.3 on 2023-07-23 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0022_alter_orderitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('Return', 'Return'), ('Processing', 'Processing'), ('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled'), ('Shipped', 'Shipped')], default='Pending', max_length=150),
        ),
    ]
