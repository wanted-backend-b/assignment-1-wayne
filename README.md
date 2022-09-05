# 📎 목차

1. [User Blog Service](#-user-blog-service)
2. [팀 인원](#-팀-인원5명)
3. [역할](#-역할)
4. [요구사항 및 분석](#-요구사항-및-분석)
5. [진행 방식](#-진행-방식)
6. [기술 스택](#-기술-스택)
7. [API Endpoints](#-api-endpoints)
8. [ERD](#-erd)
9. [참조 문서](#-참조-문서)


# 🚀 User Blog Service
- 여러 게시판과 포스팅별 조회 집계 기능을 제공하는 사이트

# 📆 개발 기간
- 2022.08.31 ~ 

# 🧑🏻‍💻 팀 인원(5명)
- 김대휘(팀장), 박민하, 윤정기, 전예솜, 조현우

# 💻 역할
#### 👉 김대휘
- PM 및 리드 개발자 역할
- 개발환경 세팅
- 프로젝트 리딩 및 코드 리뷰
#### 👉 박민하
* readme 작성
#### 👉 윤정기
- 유저 회원가입 API 구현
- 유저 로그인 API 구현
- 유저 회원탈퇴 API 구현
- 유저 @login_deco 기능 구현
#### 👉 전예솜
- 남녀별, 나이별, 시간대별 게시판 이용 통계 api 구현
- 통계 api 유닛 테스크 코드 
#### 👉 조현우
* ERD 작성
* 운영 게시판, 공지사항, 자유 게시판 API 구현
* 접근 제어 기능 구현

# 📝 요구사항 및 분석
### 1. 공지사항, 자유게시판, 운영게시판

- 권한에 따라 CRUD 권한 부여
    - 공지사항: 운영진 CRUD, 일반유저 R 권한
    - 자유 게시판 : 운영진 CRUD, 일반유저 CRUD
    - 운영 게시판: 운영진 CRUD, 일반유저 X

### 2. 회원 등급에 따른 게시판 기능 접근제어

- 일반 등급과 운영 등급으로 나누어 권한에 따른 접근제어

### 3. 회원가입, 로그인, 회원탈퇴

- JWT토큰을 이용한 회원가입, 로그인
- 회원탈퇴

### 4. 포스팅별 조회 집계
- 남여 조회 비율
- 시간대별 포스팅 조회 비율
- 나이별(10대, 20대, 30대 ..)조회 비율

# 🚡 진행 방식
- [git commit 컨벤션](https://www.notion.so/f5d4a9d98c81473e8d8fef943fced124)
- [브랜치전략](https://www.notion.so/f5d4a9d98c81473e8d8fef943fced124)

# 🛠 기술 스택
Language | Framwork | Database | HTTP | Develop | Tools
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> | <img src="https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"> | <img src="https://img.shields.io/badge/discord-5865F2?style=for-the-badge&logo=discord&logoColor=white"> <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> 

# 🎯 API Endpoints
| endpoint | HTTP Method | 기능   | require parameter                                                                                                   | response data |
|----------|-------------|------|---------------------------------------------------------------------------------------------------------------------|---------------|
| users/signup/     | POST        | 회원가입 | name: string <br/>email: string <br/>psword: string <br/>gender: string <br/>age: string <br/>phone_number: string<br/> level: string | 회원가입 성공여부     |
| users/login/      | POST        | 로그인  | email: string <br/>psword: string                                                                                         | 로그인 성공여부      |
| users/withdrawal/     | POST        | 회원탈퇴 | email: string <br/>psword: string                                                                                         | 회원탈퇴 성공여부     |
| /postings/operatings | GET | 운영 게시판 리스트 조회 | - | 운영 게시판 리스트 |
| /postings/operatings/detail | GET | 운영 게시판 상세 조회 | posting_id: int | 운영 게시판 상세 |
| /postings/operatings/detail | POST | 운영 게시판 상세 포스팅 | title: string, context: string, posting_id: int | - |
| /postings/operatings/detail | DELETE | 운영 게시판 상세 삭제 | posting_id: int | - |
| /postings/operatings/comment | POST | 운영 게시판 댓글 | comment: string, posting_id: int | - |
| /postings/notices | GET | 공지사항 게시판 리스트 조회 | - | 공지사항 게시판 리스트 |
| /postings/notices/detail | GET | 공지사항 게시판 상세 조회 | posting_id: int | 공지사항 게시판 상세 |
| /postings/notices/detail | POST | 공지사항 게시판 상세 포스팅 | title: string, context: string, posting_id: int | - |
| /postings/notices/detail | DELETE | 공지사항 게시판 상세 삭제 | posting_id: int | - |
| /postings/notices/comment | POST | 공지사항 게시판 댓글 | comment: string, posting_id: int | - |
| /postings/freeboards | GET | 자유 게시판 리스트 조회 | - | 자유 게시판 리스트 |
| /postings/freeboards/detail | GET | 자유 게시판 상세 조회 | posting_id: int | 자유 게시판 상세 |
| /postings/freeboards/detail | POST | 자유 게시판 상세 포스팅 | title: string, context: string, posting_id: int | - |
| /postings/freeboards/detail | DELETE | 자유 게시판 상세 삭제 | posting_id: int | - |
| /postings/freeboards/comment | POST | 자유 게시판 댓글 | comment: string, posting_id: int | - |
| /statistics/gender/operate | GET | 운영게시판 남녀별 이용 통계 조회| - | 남녀별 이용자 수 |
| /statistics/gender/free | GET | 자유게시판 남녀별 이용 통계 조회| - | 남녀별 이용자 수 |
| /statistics/gender/notice | GET | 공지사항 남녀별 이용 통계 조회| - | 남녀별 이용자 수 |
| /statistics/age/operate | GET | 운영게시판 나이별 이용 통계 조회| - | 나이별 이용자 수 |
| /statistics/age/free | GET | 자유게시판 나이별 이용 통계 조회| - | 나이별 이용자 수 |
| /statistics/age/notice | GET | 공지사항 나이별 이용 통계 조회| - | 나이별 이용자 수 |
| /statistics/time/operate | GET | 운영게시판 시간대별 이용 통계 조회| - | 시간대별 이용자 수 |
| /statistics/time/free | GET | 자유게시판 시간대별 이용 통계 조회| - | 시간대별 이용자 수 |
| /statistics/time/notice | GET | 공지사항 시간대별 이용 통계 조회| - | 시간대별 이용자 수 |


# 📚 ERD
![](https://velog.velcdn.com/images/miracle-21/post/349b7e0f-3a30-4c92-bd71-3634751ff24b/image.png)

# 🔖 참조 문서
- [Postman API Docs](https://documenter.getpostman.com/view/11682851/VUxVpPbo)
- [노션페이지](https://www.notion.so/Team-B-7214b88a6c54490baf57a8715f20086b)


