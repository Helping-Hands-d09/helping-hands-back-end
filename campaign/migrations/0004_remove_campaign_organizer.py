# Generated by Django 4.1 on 2022-09-10 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0003_rename_location_campaign_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='organizer',
        ),
    ]