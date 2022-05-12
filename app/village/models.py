from django.db import models
from django.contrib.postgres.fields import ArrayField

class Village(models.Model):
    id = models.CharField(
        max_length=24,
        primary_key=True
    )
    title = models.CharField(
        max_length=512
    )
    description = models.CharField(
        max_length=2048
    )
    summary = models.CharField(max_length=1024)
    image = models.CharField(
        max_length=2048
    )
    icon = models.CharField(
        max_length=512
    )
    portainer_jwt = models.CharField(
        max_length=4096,
        default=None, blank=True, null=True
    )


class Exercise(models.Model):
    id = models.CharField(
        max_length=24,
        primary_key=True
    )
    village = models.ForeignKey(
        Village, 
        on_delete=models.PROTECT,
        default=None
    )
    title = models.CharField(
        max_length=512
    )
    description = models.CharField(
        max_length=2048
    )
    summary = models.CharField(max_length=1024)
    steps = ArrayField(
        models.CharField(max_length=2048)
    )
    portainer_server = models.CharField(max_length=64)
    portainer_stack_id = models.CharField(max_length=64)
    portainer_ip = models.CharField(max_length=64)
    portainer_link = models.CharField(max_length=256)

