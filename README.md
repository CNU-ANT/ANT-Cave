# ANT Cave ANT 동아리 홈페이지

ANT 동아리 홈페이지를 작성하는 페이지입니다. Django framework를 기반으로 만들어집니다.


## 1) 설치
---------
1. Postgres를 설치한다.
	* Window 유저
		* [Postgres 설치](www.enterprisedb.com/products-services-training/pgdownload#windows)
		- port 번호 : 5432
		- 비밀번호 : su6407
		시스템 환경변수 설정-환경변수-Path-C:\Program Files\PostgreSQL\bin - 환경변수 추가
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
