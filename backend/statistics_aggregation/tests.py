import json
import jwt
import os

from django.test import TestCase, Client
from users.models import Updated_time

from postings.models import FreeBoardPosting, FreeView
from postings.models import OperatingBoardPosting, OperatingView
from postings.models import NoticeBoardPosting, NoticeView
from users.models import User


class StatisticFreeView(TestCase):
    @classmethod
    def setUpTestData(cls):

        User.objects.create(
            id=1,
            email="aasdfa@naver.com",
            psword="123AAV@@#",
            name="홍길동",
            level=1,
            gender="남",
            age=23,
            phone_number="010-2222-3333",
        )

        FreeBoardPosting.objects.create(
            id=1, title="Hi", context="Hi", user=User.objects.get(id=1)
        )

        FreeView.objects.create(
            id=1,
            user=User.objects.get(id=1),
            free_board_posting=FreeBoardPosting.objects.get(id=1),
        )

        cls.token = jwt.encode(
            {"user_id": User.objects.get(id=1).id},
            os.environ.get("SECRET"),
            os.environ.get("ALGORITHM"),
        )

    # 자유게시판에 글을 등록한 사람의 남녀별 집계 api 테스트
    def test_free_gender_view(self):
        client = Client()
        header = {"HTTP_Authorization": self.token}
        response = client.get(
            "/statistics/gender/free/",
            **header,
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"result": {"M": 1, "F": 0}},
        )

    # 자유게시판에 글을 등록한 사람의 나이대별 집계 api 테스트
    def test_free_age_view(self):
        client = Client()
        header = {"HTTP_Authorization": self.token}
        response = client.get(
            "/statistics/age/free/", **header, content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "result": {
                    "10": 0,
                    "20": 1,
                    "30": 0,
                    "40": 0,
                    "50": 0,
                    "60": 0,
                    "70": 0,
                    "80": 0,
                    "90": 0,
                }
            },
        )

    # 자유게시판의 글을 조회한 시간대별 집계 api unit test
    def test_free_time_view(self):
        Updated_time.objects.create(user=User.objects.get(id=1))
        update_time_obj = Updated_time.objects.get(user=User.objects.get(id=1))

        client = Client()
        header = {"HTTP_Authorization": self.token}
        response = client.get(
            "/statistics/time/free/", **header, content_type="application/json"
        )

        result = {}

        for i in range(1, 25):
            result[str(i)] = 0

        key = str(update_time_obj.modified_at.hour)
        result[key] = result[key] + 1

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"result": result},
        )


class StatisticOperateView(TestCase):
    @classmethod
    def setUpTestData(cls):

        User.objects.create(
            id=1,
            email="aasdfa@naver.com",
            psword="123AAV@@#",
            name="홍길동",
            level=1,
            gender="남",
            age=23,
            phone_number="010-2222-3333",
        )

        OperatingBoardPosting.objects.create(
            id=1, title="Hi", context="Hi", user=User.objects.get(id=1)
        )

        OperatingView.objects.create(
            id=1,
            user=User.objects.get(id=1),
            operating_board_posting=OperatingBoardPosting.objects.get(id=1),
        )

        cls.token = jwt.encode(
            {"user_id": User.objects.get(id=1).id},
            os.environ.get("SECRET"),
            os.environ.get("ALGORITHM"),
        )

    # 운영게시판에 글을 등록한 사람의 남녀별 집계 api 테스트
    def test_operate_gender_view(self):
        client = Client()
        header = {"HTTP_Authorization": self.token}
        response = client.get(
            "/statistics/gender/operate/",
            **header,
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"result": {"M": 1, "F": 0}},
        )

    # 운영게시판에 글을 등록한 사람의 나이별 집계 api unit test
    def test_opeate_age_view(self):
        client = Client()
        header = {"HTTP_Authorization": self.token}
        response = client.get(
            "/statistics/age/operate/",
            **header,
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "result": {
                    "10": 0,
                    "20": 1,
                    "30": 0,
                    "40": 0,
                    "50": 0,
                    "60": 0,
                    "70": 0,
                    "80": 0,
                    "90": 0,
                }
            },
        )

    # 운영게시판의 글을 조회한 시간대별 집계 api unit test
    def test_operate_time_view(self):
        Updated_time.objects.create(user=User.objects.get(id=1))
        update_time_obj = Updated_time.objects.get(user=User.objects.get(id=1))

        client = Client()
        header = {"HTTP_Authorization": self.token}
        response = client.get(
            "/statistics/time/operate/",
            **header,
            content_type="application/json"
        )

        result = {}

        for i in range(1, 25):
            result[str(i)] = 0

        key = str(update_time_obj.modified_at.hour)
        result[key] = result[key] + 1

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"result": result},
        )


class StatisticNoticeView(TestCase):
    @classmethod
    def setUpTestData(cls):

        User.objects.create(
            id=1,
            email="aasdfa@naver.com",
            psword="123AAV@@#",
            name="홍길동",
            level=1,
            gender="남",
            age=23,
            phone_number="010-2222-3333",
        )

        NoticeBoardPosting.objects.create(
            id=1, title="Hi", context="Hi", user=User.objects.get(id=1)
        )

        NoticeView.objects.create(
            id=1,
            user=User.objects.get(id=1),
            notice_posting=NoticeBoardPosting.objects.get(id=1),
        )

        cls.token = jwt.encode(
            {"user_id": User.objects.get(id=1).id},
            os.environ.get("SECRET"),
            os.environ.get("ALGORITHM"),
        )

    # 공지사항에 글을 등록한 사람의 남녀별 집계 api 테스트
    def test_notice_gender_view(self):
        client = Client()
        header = {"HTTP_Authorization": self.token}
        response = client.get(
            "/statistics/gender/notice/",
            **header,
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"result": {"M": 1, "F": 0}},
        )

    # 공지사항에 글을 등록한 사람의 나이별 집계 api unit test
    def test_notice_age_view(self):
        client = Client()
        header = {"HTTP_Authorization": self.token}
        response = client.get(
            "/statistics/age/notice/",
            **header,
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "result": {
                    "10": 0,
                    "20": 1,
                    "30": 0,
                    "40": 0,
                    "50": 0,
                    "60": 0,
                    "70": 0,
                    "80": 0,
                    "90": 0,
                }
            },
        )

    # 운영게시판의 글을 조회한 시간대별 집계 api unit test
    def test_notice_time_view(self):
        Updated_time.objects.create(user=User.objects.get(id=1))
        update_time_obj = Updated_time.objects.get(user=User.objects.get(id=1))

        client = Client()
        header = {"HTTP_Authorization": self.token}
        response = client.get(
            "/statistics/time/notice/",
            **header,
            content_type="application/json"
        )

        result = {}

        for i in range(1, 25):
            result[str(i)] = 0

        key = str(update_time_obj.modified_at.hour)
        result[key] = result[key] + 1

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"result": result},
        )
