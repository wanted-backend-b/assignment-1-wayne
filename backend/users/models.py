from django.db import models

from core.models import TimeStampCreateModel, TimeStampModifyModel

GENDER_CHOICES = [
    ("f", "female"),
    ("m", "male"),
]


class User(TimeStampCreateModel):
    email = models.CharField(max_length=100)
    psword = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100, default=1)  # 일반권한(1)로 기본 권한 설정
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    class Meta:
        db_table = "users"


class UpdatedTime(TimeStampModifyModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "update_time"
