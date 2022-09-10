# Generated by Django 4.1 on 2022-09-10 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0008_delete_joined_campaigns'),
        ('campaign', '0005_joinedcampaign_campaign_organizer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joinedcampaign',
            name='title',
        ),
        migrations.AddField(
            model_name='campaign',
            name='comments',
            field=models.ManyToManyField(related_name='comments', through='campaign.JoinedCampaign', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='joinedcampaign',
            name='campaign',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to='campaign.campaign'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='joinedcampaign',
            name='member',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]