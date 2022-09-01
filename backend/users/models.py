from django.db import models

from core.models import TimeStampCreateModel, TimeStampModifyModel
import postings

class User(TimeStampCreateModel):
    email           = models.CharField(max_length=100)
    psword          = models.CharField(max_length=100)
    name            = models.CharField(max_length=100)
    level           = models.CharField(max_length=100, default=1)
    gender          = models.CharField(max_length=100)
    age             = models.CharField(max_length=100)
    phone_number    = models.CharField(max_length=100)
    notice          = models.ForeignKey("postings.NoticeBoardPosting", on_delete=models.CASCADE)
    free_board      = models.ForeignKey("postings.FreeBoardPosting", on_delete=models.CASCADE)
    operation_board = models.ForeignKey("postings.OperatingBoardPosting", on_delete=models.CASCADE)

    class Meta:
        db_table = "users"

class Updated_time(TimeStampModifyModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "update_time"