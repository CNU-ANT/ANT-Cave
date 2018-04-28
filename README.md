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
### Python Library<br>
선택) Library 의존성 관리를 위해 가상환경으로 설치 추천 (venv)
```
python -m venv ant-cave
ant-cave/Scripts/activate
```
필수) 홈 디렉터리에서 
```
pip install -r requirement.txt 
```
* [라이브러리 목록](https://github.com/CNU-ANT/ANT-Cave/blob/master/requirements.txt)
---------
### DB
1. Postgres를 설치한다.
	* Window 유저
		* [Postgres 설치(10.3 version)](https://www.enterprisedb.com/products-services-training/pgdownload#windows)
		- port 번호 : 5432
		- 비밀번호 : su6407
		시스템 환경변수 설정-환경변수-Path-C:\Program Files\PostgreSQL\10\bin - 환경변수 추가(각자 파일 위치 확인하시고 적용하세요)
		```bash
		psql --username=postgres
		``` 

	* Linux 유저
		``` bash
		sudo apt-get install postgresql postgresql-contrib
		```
2. Database 생성한다.
	1 ) postgres를 실행한다.
	* Window 유저
	```bash
	psql --username=postgres
	```
		를 통해 들어가고 이전에 설정한 패스워드를 입력한다.

	* Linux 유저
	```bash
	sudo -u postgres psql
	```
		위의 명령어를 이용해 psql를 관리자 권한으로 연다.
		
	2 ) 데이터베이스를 생성한다.
	```sql
	CREATE USER khz;
	CREATE DATABASE antcave OWNER khz;
	```

3. DATABASE migrate 한다.
	```bash
	python manage.py makemigrations <app_name>
	python manage.py migrate
	```
	app_name은 Board와 Profile을 넣어주면 됩니다.
	두 app 을 모두 makemigrations 해준 후 migrate 하면 됩니다.

4. DB가 제대로 생성되었는지 확인.
	```bash
	python manage.py dbshell
	\dt
	```
	를 통해서 디비가 잘 생성되었는지 확인 할수 있다.

+ 주의
	migrations 폴더를 지우지 마세요.
	
