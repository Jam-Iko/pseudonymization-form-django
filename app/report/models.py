from django.db import models
import uuid

class ReportModel(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    malware_name = models.CharField(
        max_length=256
    )
    category = models.CharField(
        max_length=256
    )
    group = models.CharField(
        max_length=256
    )
    investigator_name = models.CharField(
        max_length=128
    )
    started = models.DateTimeField(
        blank=True, 
        null=True
    )
    ended = models.DateTimeField(
        blank=True, 
        null=True
    )
    summary = models.TextField(
        max_length=2048,
        null=False, 
        blank=False
    )


class ReportFilesModel(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    report = models.ForeignKey(
        ReportModel, 
        on_delete=models.CASCADE
    )
    file = models.CharField(
        max_length=256,
        null=True, 
        blank=True
    )
    hash = models.CharField(
        max_length=256,
        null=True, 
        blank=True
    )
    notes = models.TextField(
        max_length=2048,
        null=True, 
        blank=True
    )


class ReportConnectionsModel(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    report = models.ForeignKey(
        ReportModel, 
        on_delete=models.CASCADE
    )
    ip = models.GenericIPAddressField(
        protocol='both', 
        unpack_ipv4=False,
        blank=True,
        null=True,
    )
    url = models.URLField(
        max_length=2048,
        blank=True,
        null=True
    )
    notes = models.TextField(
        max_length=2048,
        blank=True,
        null=True
    )
