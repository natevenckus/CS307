# Generated by Django 2.1.7 on 2019-04-02 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0003_riderlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='Ride',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='driver.RiderLink'),
        ),
    ]