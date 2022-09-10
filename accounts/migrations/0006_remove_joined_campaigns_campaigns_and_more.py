# Generated by Django 4.1 on 2022-09-10 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0004_remove_campaign_organizer'),
        ('accounts', '0005_joined_campaigns'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joined_campaigns',
            name='campaigns',
        ),
        migrations.RemoveField(
            model_name='joined_campaigns',
            name='user',
        ),
        migrations.AddField(
            model_name='joined_campaigns',
            name='campaigns',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='campaign.campaign'),
        ),
        migrations.AddField(
            model_name='joined_campaigns',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
