# Generated by Django 4.2.1 on 2023-06-04 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_alter_item_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('Sold', 'Sold'), ('Cancelled', 'Cancelled'), ('In-auction', 'In-auction')], default='In-auction', max_length=100),
        ),
    ]
