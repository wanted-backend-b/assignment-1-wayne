from django.db import models


class TimeStampCreateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class TimeStampModifyModel(models.Model):
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
