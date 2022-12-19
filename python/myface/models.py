from email.policy import default
from django.db import models
from django.conf import settings
# from django_cleanup import cleanup
# Create your models here.
class PhotoList(models.Model):

    class Meta:
        db_table = "photolist"
    photo = models.ImageField(verbose_name="フォト",upload_to="photo/")
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
