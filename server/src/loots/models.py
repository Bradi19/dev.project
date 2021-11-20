from django.db import models
from server.src.bettings import models as bettings
from django.core.validators import FileExtensionValidator
from server.base.services import get_path_upload_avatar, validate_size_image
class Loots(models.Model):
    join_date = models.DateTimeField(auto_now_add=True)
    attributes = models.JSONField(null=True)
    image = models.ImageField(
        upload_to=get_path_upload_avatar,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(
            allowed_extensions=['jpg']), validate_size_image]
    )

class LanguageAll(models.Model):
    lang = models.CharField(max_length=50)


class LngDesc(models.Model):
    loots = models.ForeignKey(Loots, on_delete=models.CASCADE)
    lang = models.ForeignKey(LanguageAll, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    meta_name = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    meta_description = models.CharField(max_length=150)
    keyboards = models.CharField(max_length=200)
class BettingsLoot(models.Model):
    loots = models.ForeignKey(Loots, on_delete=models.CASCADE)
    bettings = models.ForeignKey(bettings.Bettings, on_delete=models.CASCADE)