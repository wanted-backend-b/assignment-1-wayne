from django.db import models

from core.models import TimeStampCreateModel, TimeStampModel
from users.models import User

# 공지사항 모델링


class NoticeBoardPosting(TimeStampCreateModel):
    title = models.CharField(max_length=100)
    context = models.CharField(max_length=500)
    view = models.ManyToManyField(
        User, through="NoticeView", related_name="notice_view"
    )
    comment = models.ManyToManyField(
        User, through="NoticeComment", related_name="notice_comment"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = "notices_boards"


class NoticeView(TimeStampCreateModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notice_posting = models.ForeignKey(NoticeBoardPosting, on_delete=models.CASCADE)

    class Meta:
        db_table = "notices_views"


class NoticeComment(TimeStampModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notice_posting = models.ForeignKey(NoticeBoardPosting, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)

    class Meta:
        db_table = "notices_comments"


# 자유게시판 모델링


class FreeBoardPosting(TimeStampCreateModel):
    title = models.CharField(max_length=100)
    context = models.CharField(max_length=500)
    view = models.ManyToManyField(User, through="FreeView", related_name="posting_view")
    comment = models.ManyToManyField(
        User, through="FreeComment", related_name="posting_comment"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = "free_boards"


class FreeView(TimeStampCreateModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    free_board_posting = models.ForeignKey(FreeBoardPosting, on_delete=models.CASCADE)

    class Meta:
        db_table = "free_views"


class FreeComment(TimeStampModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    free_board_posting = models.ForeignKey(FreeBoardPosting, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)

    class Meta:
        db_table = "free_comments"


# 운영게시판 모델링


class OperatingBoardPosting(TimeStampCreateModel):
    title = models.CharField(max_length=100)
    context = models.CharField(max_length=500)
    view = models.ManyToManyField(
        User, through="OperatingView", related_name="operating_view"
    )
    comment = models.ManyToManyField(
        User, through="OperatingComment", related_name="operatin_comment"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = "operating_boards"


class OperatingView(TimeStampCreateModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    operating_board_posting = models.ForeignKey(
        OperatingBoardPosting, on_delete=models.CASCADE
    )

    class Meta:
        db_table = "operating_views"


class OperatingComment(TimeStampModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    operating_board_posting = models.ForeignKey(
        OperatingBoardPosting, on_delete=models.CASCADE
    )
    comment = models.CharField(max_length=300)

    class Meta:
        db_table = "operating_comments"
