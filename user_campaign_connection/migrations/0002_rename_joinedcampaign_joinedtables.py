# Generated by Django 4.1 on 2022-09-11 12:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('campaign', '0008_alter_campaign_organizer'),
        ('user_campaign_connection', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='JoinedCampaign',
            new_name='JoinedTables',
        ),
    ]
