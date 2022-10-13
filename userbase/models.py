from django.db import models
import uuid

class PublicKeys(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    public_key = models.TextField(unique=True)
    username = models.CharField(unique=True,max_length = 255)

