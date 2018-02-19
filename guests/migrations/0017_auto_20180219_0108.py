# Generated by Django 2.0.2 on 2018-02-19 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0016_party_rehearsal_dinner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='save_the_date_opened',
        ),
        migrations.RemoveField(
            model_name='party',
            name='save_the_date_sent',
        ),
        migrations.AlterField(
            model_name='guest',
            name='meal',
            field=models.CharField(blank=True, choices=[('meat', 'meat'), ('vegetarian', 'vegetarian')], max_length=20, null=True),
        ),
    ]
