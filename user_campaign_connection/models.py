from django.db import models
from django.contrib.auth import get_user_model
from campaign.models import Campaign

# Create your models here.

# class Testing(models.Model):
#     """
#     The connection between the users and the campaigns (joining)
#     """
#     campaigns = models.ManyToManyField(Campaign, through='JoinedCampaign',through_fields=('campaign' ,'member'), related_name='campaigns')

class JoinedTables(models.Model): 
    """
    The connection between the users and the campaigns (joining) 
    """
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='campaign')
    member = models.ForeignKey(get_user_model(), null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"connection c_id{self.campaign} m_id{self.member}"

