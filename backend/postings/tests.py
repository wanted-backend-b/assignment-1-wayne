import json
import jwt
import os

from django.test import TestCase, Client

from postings.models import FreeBoardPosting, FreeComment, FreeView
from users.models    import User


# 자유게시판 리스트 API unit test
class FreeBoardListView(TestCase):
    def setUp(self):
        User.objects.create(
            id              = 1,
            email           = 'aasdfa@naver.com',
            psword          = '123AAV@@#',
            name            = '홍길동',
            level           = 1,
            gender          = '남',
            age             = 23,
            phone_number    = '010-2222-3333',
        )

        FreeBoardPosting.objects.create(
            id      = 1,
            title   = 'Hi',
            context = 'Hi',
            user    = User.objects.get(id=1)
        )

        FreeComment.objects.create(
            id                 = 1,
            user               = User.objects.get(id=1),
            free_board_posting = FreeBoardPosting.objects.get(id=1),
            comment            = "AAAA"
        )

        FreeView.objects.create(
            id                 = 1,
            user               = User.objects.get(id=1),
            free_board_posting = FreeBoardPosting.objects.get(id=1),
        )

        self.token = jwt.encode({'user_id':User.objects.get(id=1).id}, os.environ.get("SECRET"), 
                        os.environ.get("ALGORITHM"))

    def tearDown(self):
        User.objects.all().delete()
        FreeBoardPosting.objects.all().delete()
        FreeComment.objects.all().delete()
        FreeView.objects.all().delete()

    # 자유게시판 리스트 조회 API unit test
    def test_success_list_view_get(self):
        client   = Client()
        header   = {"HTTP_Authorization" : self.token}
        response = client.get("/postings/freeboards", **header, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'results' : [{
            'id'      : 1,
            'title'   : 'Hi',
            'context' : 'Hi',
            'views'   : 1
        }]})


# 자유게시판 상세 API unit test
class FreeBoardDetailView(TestCase):
    def setUp(self):
        User.objects.create(
            id              = 1,
            email           = 'aasdfa@naver.com',
            psword          = '123AAV@@#',
            name            = '홍길동',
            level           = 1,
            gender          = '남',
            age             = 23,
            phone_number    = '010-2222-3333',
        )

        FreeBoardPosting.objects.create(
            id      = 1,
            title   = 'Hi',
            context = 'Hi',
            user    = User.objects.get(id=1)
        )

        FreeComment.objects.create(
            id                 = 1,
            user               = User.objects.get(id=1),
            free_board_posting = FreeBoardPosting.objects.get(id=1),
            comment            = "AAAA"
        )

        FreeView.objects.create(
            id                 = 1,
            user               = User.objects.get(id=1),
            free_board_posting = FreeBoardPosting.objects.get(id=1),
        )

        self.token = jwt.encode({'user_id':User.objects.get(id=1).id}, os.environ.get("SECRET"), 
                        os.environ.get("ALGORITHM"))

    def tearDown(self):
        User.objects.all().delete()
        FreeBoardPosting.objects.all().delete()
        FreeComment.objects.all().delete()
        FreeView.objects.all().delete()

    # 자유게시판 상세 조회 API unit test
    def test_success_detail_view_get(self):
        client   = Client()
        header   = {"HTTP_Authorization" : self.token}
        response = client.get("/postings/freeboards/detail/1", **header, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result":{
                'id'       : 1,
                'title'    : 'Hi',
                'context'  : 'Hi',
                'views'    : 1,
                'comments' : ["AAAA"]
            }})

    # 자유게시판 상세 포스팅 API unit test
    def test_success_detail_view_post(self):
        client   = Client()
        header   = {"HTTP_Authorization" : self.token}
        body     = {
            "title" : "Hello",
            "context": "Hello There"
        }

        response = client.post("/postings/freeboards/detail", **header, content_type='application/json',
                        data=json.dumps(body))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"message" : "SUCCESS"})

    # 자유게시판 상세 삭제 API unit test
    def test_success_detail_view_delete(self):
        client   = Client()
        header   = {"HTTP_Authorization" : self.token}
        body     = {
            "posting_id" : 1
        }

        response = client.delete("/postings/freeboards/detail", **header, content_type='application/json',
                        data=json.dumps(body))

        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.json(), {"message" : "DATA_DELETED"})


# 자유게시판 댓글 API unit test
class FreeBoardCommentView(TestCase):
    def setUp(self):
        User.objects.create(
            id              = 1,
            email           = 'aasdfa@naver.com',
            psword          = '123AAV@@#',
            name            = '홍길동',
            level           = 1,
            gender          = '남',
            age             = 23,
            phone_number    = '010-2222-3333',
        )

        FreeBoardPosting.objects.create(
            id      = 1,
            title   = 'Hi',
            context = 'Hi',
            user    = User.objects.get(id=1)
        )

        self.token = jwt.encode({'user_id':User.objects.get(id=1).id}, os.environ.get("SECRET"), 
                        os.environ.get("ALGORITHM"))

    def tearDown(self):
        User.objects.all().delete()
        FreeBoardPosting.objects.all().delete()
        FreeComment.objects.all().delete()
        FreeView.objects.all().delete()

    # 자유게시판 댓글 포스팅 API unit test
    def test_success_comment_view_post(self):
        client   = Client()
        header   = {"HTTP_Authorization" : self.token}
        body     = {
            "comment"    : "Hello",
            "posting_id" : 1
        }

        response = client.post("/postings/freeboards/comment", **header, 
                    content_type='application/json',
                    data=json.dumps(body))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"message" : "SUCCESS"})


# 자유게시판 조회 API unit test
class FreeBoardView(TestCase):
    def setUp(self):
        User.objects.create(
            id              = 1,
            email           = 'aasdfa@naver.com',
            psword          = '123AAV@@#',
            name            = '홍길동',
            level           = 1,
            gender          = '남',
            age             = 23,
            phone_number    = '010-2222-3333',
        )

        FreeBoardPosting.objects.create(
            id      = 1,
            title   = 'Hi',
            context = 'Hi',
            user    = User.objects.get(id=1)
        )

        self.token = jwt.encode({'user_id':User.objects.get(id=1).id}, os.environ.get("SECRET"), 
                        os.environ.get("ALGORITHM"))

    def tearDown(self):
        User.objects.all().delete()
        FreeBoardPosting.objects.all().delete()
        FreeComment.objects.all().delete()
        FreeView.objects.all().delete()

    # 자유게시판 댓글 포스팅 API unit test
    def test_success_view_post(self):
        client   = Client()
        header   = {"HTTP_Authorization" : self.token}
        body     = {
            "posting_id" : 1
        }

        response = client.post("/postings/freeboards/view", **header, 
                    content_type='application/json',
                    data=json.dumps(body))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'message' : 'SUCCESS', 'count' : 1})