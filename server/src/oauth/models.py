from django.db import models
from django.core.validators import FileExtensionValidator
from server.base.services import get_path_upload_avatar, validate_size_image


class AuthUser(models.Model):
    email = models.EmailField(max_length=150, unique=True)
    join_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(max_length=2000, blank=True, null=True)
    display_name = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(
        upload_to=get_path_upload_avatar,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(
            allowed_extensions=['jpg']), validate_size_image]
    )

    @property
    def is_authentificated(self):
        return True

    def __str__(self):
        return self.email


class LootsUser(models.Model):
    join_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)


class BettingsUser(models.Model):
    join_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)