from django.db import models
from server.src.loots import models as lootss
from server.src.oauth import models as oauth
import datetime 
class Bettings(models.Model):
    betting = models.FloatField()
    join_date = models.DateTimeField(auto_now_add=True)
    live_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=(datetime.date.today()+datetime.timedelta(4)))
    better = models.BooleanField(default=True)
class UserBettings(models.Model):
    bettings = models.ForeignKey(oauth.AuthUser, on_delete=models.CASCADE)
class Bettingsdesc(models.Model):
    bettings = models.ForeignKey(Bettings, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    meta_name = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    meta_description = models.CharField(max_length=150)
    keyboards = models.CharField(max_length=200)