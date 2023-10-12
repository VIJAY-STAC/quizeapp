import uuid
from django.db import models
from django.conf import settings

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        abstract = True



class PrimaryUUIDModel(models.Model):
    # id = models.AutoField(primary_key=True,)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    
    class Meta(object):
        abstract = True


class PrimaryUUIDTimeStampedModel(PrimaryUUIDModel, TimeStampedModel):
    class Meta(object):
        abstract = True