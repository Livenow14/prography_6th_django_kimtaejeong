# 프로그라피 6기 DRF 사전과제


## 사용 기술
* Django Rest Framework
* Django 2.1.2 
* AWS EC2_Amazon Linux AMI 1
* AWS RDS (Maria DB)
* nginx

## 현재 링크에 엑세스만 하시면 모든사용자가 CRUD 가능합니다. 
* (보안상 문제가 살짝 걱정되긴 합니다 -> 커밋 종료 이후에도 추가할 예정 )

# 기능설명
### 게시글 전체 리스트 확인 
```groovy
http://ec2-15-165-113-25.ap-northeast-2.compute.amazonaws.com/crud_list/
```

```groovy
  
{
    "count": 5,
    "next": "http://ec2-15-165-113-25.ap-northeast-2.compute.amazonaws.com/crud_list/?page=2",
    "previous": null,
    "results": [
        {
            "id": 5,
            "title": "4번째",
            "description": "4번째",
            "created_at": "2020-03-05T04:46:12+09:00"
        },
        {
            "id": 4,
            "title": "4번째",
            "description": "4번째",
            "created_at": "2020-03-05T04:46:10+09:00"
        },
        {
            "id": 3,
            "title": "3번째",
            "description": "3번째",
            "created_at": "2020-03-05T04:46:04+09:00"
        }
    ]
}

```

### 게시글 상세 정보 확인
```groovy
http://ec2-15-165-113-25.ap-northeast-2.compute.amazonaws.com/crud_list/{id}
```
```groovy
{
    "id": 1,
    "title": "첫번째",
    "description": "첫번째",
    "created_at": "2020-03-05T04:33:31+09:00",
    "updated_at": "2020-03-05T04:33:31+09:00"
}
```

### 게시글 만들기
```groovy
http://ec2-15-165-113-25.ap-northeast-2.compute.amazonaws.com/crud_list/create
```

### 게시글 수정하기
```groovy
http://ec2-15-165-113-25.ap-northeast-2.compute.amazonaws.com/crud_list/{id}/update
```

### 게시글 삭제하기
```groovy
http://ec2-15-165-113-25.ap-northeast-2.compute.amazonaws.com/crud_list/{id}/delete
```

### 로그인, 로그아웃
구현을 하였지만 ,아직 완벽하게 구현을 하지 못한 상태입니다. 
```groovy
http://ec2-15-165-113-25.ap-northeast-2.compute.amazonaws.com/rest-auth/registration
```
을 통해 등록하고 
```groovy
http://ec2-15-165-113-25.ap-northeast-2.compute.amazonaws.com/rest-auth/lgoin
```
을 통해 로그인 할 수 있지만. 
등록, 로그인 이후의 과정을 작성하지 않아 500에러가 발생합니다. 

서버 배포를 무중단으로 하려고 하나 완벽히 만들지 못한 관계로.
면접 전까지만 배포할 계획입니다. 

------- 배포중단 ---------
