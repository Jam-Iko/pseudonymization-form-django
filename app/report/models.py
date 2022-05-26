from django.db import models
import uuid

class ReportModel(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    malware_name = models.CharField(
        max_length=24
    )
    category = models.CharField(
        max_length=24
    )
    group = models.CharField(
        max_length=24
    )
    investigator_name = models.CharField(
        max_length=24
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
        max_length=24,
        null=True, 
        blank=True
    )
    hash = models.CharField(
        max_length=24,
        null=True, 
        blank=True
    )
    notes = models.TextField(
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
    ip = models.CharField(
        max_length=24,
        blank=True,
        null=True
    )
    url = models.URLField(
        blank=True,
        null=True
    )
    notes = models.TextField(
        blank=True,
        null=True
    )
