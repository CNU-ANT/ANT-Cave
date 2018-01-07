# ANT Cave ANT 동아리 홈페이지

ANT 동아리 홈페이지를 작성하는 페이지입니다. Django framework를 기반으로 만들어집니다.

장고 따라하기   
- https://docs.djangoproject.com/ko/2.0/intro/tutorial01/
- https://www.djangoproject.com/start/

Html, Css 해보기 
- https://www.codecademy.com/learn/learn-html
- https://www.codecademy.com/learn/learn-css


웹 관련 doc 
- https://www.w3schools.com/
- https://www.w3schools.com/bootstrap4/default.asp
 bootstrap (미리 만들어준 css 모듈)
 
Readme 작성법 
- https://gist.github.com/ihoneymon/652be052a0727ad59601 
- (미리보기) https://stackedit.io/editor

## 1) 설치
---------
1. Postgres를 설치한다.
	* Window 유저
		* [Postgres 설치(10.3 version)](https://www.enterprisedb.com/products-services-training/pgdownload#windows)
		- port 번호 : 5432
		- 비밀번호 : su6407
		시스템 환경변수 설정-환경변수-Path-C:\Program Files\PostgreSQL\10\bin - 환경변수 추가(각자 파일 위치 확인하시고 적용하세요)
		```bash
		psql --username=postgres
		``` 

	* Ubuntu 유저
		``` bash
		sudo apt-get install postgresql postgresql-contrib
		```
2. Database 생성한다.
```bash
CREATE USER khz;
CREATE DATABASE antcave OWNER khz;
```
