from django.db import models

# Create your models here.
from django.db import models

from core.models  import TimeStampCreateModel, TimeStampModifyModel, TimeStampModel
from users.models import User

# 공지사항 모델링

class NoticeBoard(TimeStampCreateModel):
    notice_posting = models.ForeignKey("NoticeBoardPosting", on_delete=models.CASCADE)

    class Meta:
        db_table = "notices_boards"

class NoticeBoardPosting(TimeStampCreateModel):
    title   = models.CharField(max_length=100)
    context = models.CharField(max_length=500)
    view    = models.ManyToManyField(User, through="NoticeView")
    comment = models.ManyToManyField(User, through="NoticeComment")

    class Meta:
        db_table = "notices_boards"

class NoticeView(TimeStampCreateModel):
    user           = models.ForeignKey(User, on_delete=models.CASCADE)
    notice_posting = models.ForeignKey(NoticeBoardPosting, on_delete=models.CASCADE)

    class Meta:
        db_table = "notices_views"

class NoticeComment(TimeStampModel):
    user           = models.ForeignKey(User, on_delete=models.CASCADE)
    notice_posting = models.ForeignKey(NoticeBoardPosting, on_delete=models.CASCADE)
    comment        = models.CharField(max_length=300)

    class Meta:
        db_table = "notices_comments"

# 자유게시판 모델링

class FreeBoard(TimeStampCreateModel):
    free_board_posting = models.ForeignKey("FreeBoardPosting", on_delete=models.CASCADE)

    class Meta:
        db_table = "free_boards"

class FreeBoardPosting(TimeStampCreateModel):
    title   = models.CharField(max_length=100)
    context = models.CharField(max_length=500)
    view    = models.ManyToManyField(User, through="FreeView")
    comment = models.ManyToManyField(User, through="FreeComment")

    class Meta:
        db_table = "free_boards"

class FreeView(TimeStampCreateModel):
    user               = models.ForeignKey(User, on_delete=models.CASCADE)
    free_board_posting = models.ForeignKey(FreeBoardPosting, on_delete=models.CASCADE)

    class Meta:
        db_table = "free_views"

class FreeComment(TimeStampModel):
    user               = models.ForeignKey(User, on_delete=models.CASCADE)
    free_board_posting = models.ForeignKey(FreeBoardPosting, on_delete=models.CASCADE)
    comment            = models.CharField(max_length=300)

    class Meta:
        db_table = "free_comments"

# 운영게시판 모델링

class OperatingBoard(TimeStampCreateModel):
    operating_board_posting = models.ForeignKey("OperatingBoardPosting", on_delete=models.CASCADE)

    class Meta:
        db_table = "operating_boards"

class OperatingBoardPosting(TimeStampCreateModel):
    title   = models.CharField(max_length=100)
    context = models.CharField(max_length=500)
    view    = models.ManyToManyField(User, through="OperatingView")
    comment = models.ManyToManyField(User, through="OperatingComment")

    class Meta:
        db_table = "operating_boards"

class OperatingView(TimeStampCreateModel):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    operating_board_posting = models.ForeignKey(OperatingBoardPosting, on_delete=models.CASCADE)

    class Meta:
        db_table = "operating_views"

class OperatingComment(TimeStampModel):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    operating_board_posting = models.ForeignKey(OperatingBoardPosting, on_delete=models.CASCADE)
    comment                 = models.CharField(max_length=300)

    class Meta:
        db_table = "operating_comments"