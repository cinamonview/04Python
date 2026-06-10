/*
MariaDB에서 새로운 데이터베이스와  계정 생성하기 :
	오라클 에서는 계정만 생성하면 되지만 MySQL(MariaDB)에서는
	DB와 User(사용자계정)을 동시에 생성한 후 
	권한설정을 해야 한다. 
*/
# DB와 사용자계정 생성>> mysql DB에서 root로 로그인한 후 실행

## 아래 작업은 root계정으로 접속한 후 실행해야 한다 ##

#새로운 데이터베이스 생성
CREATE DATABASE sample_db;
# 새로운 사용자계정 생성(로컬에서만 접속할 수 있게 설정)
CREATE USER 'sample_user'@'localhost' IDENTIFIED BY '1234';
# sample_db를 사용할 수 있는 모든 권한을 sample_user에게 부여한다.
GRANT ALL PRIVILEGES ON sample_db.* TO 'sample_user'@'localhost';
# 이 명령을 통해 위에서 설정한 사항을 MariaDB에 적용
FLUSH PRIVILEGES;

/*
실행방법
f9:
	현재 문서의 전체 쿼리문을 한꺼번에 실행
ctrl f9 :
	블럭으로 지정한 쿼리문만 실행.
	만약 쿼리문의절반정도만 선택했다면, 실행시 에러가 발생한다.
ctrl shift f9 :
	현재 쿼리를 실행한다. 단 마지막에 작성한
	문장의 세미콜론 안으로 커서를 옮긴 후 실행해야 한다.
*/

SELECT * FROM  board;

SELECT * FROM  books;

SELECT * FROM  guestbook;

###########################################################
## 여기서부터는 sample_user 계정으로 접속한후 작성합니다 ##

/*
AUTO_INCREMENT :
	자동증가 컬럼으로 지정한다. 오라클에서 사용하는 
	Sequence(시퀀스)와 동일한 역할로, 1씩 증가하는 순차적인 
	정수값을 자동으로 생성 후 입력하게 된다.

UNSINGED :
	 정수형 컬럼으로 지정하는 경우 음수는 사용하지 않고,
	 양수의 범위만 사용한다. 이때 양의 범위가 2배로 늘어난다.
*/

CREATE TABLE tb_int (
	/* 일련번호 */
	idx INT PRIMARY KEY AUTO_INCREMENT,
	/* 정수형 */
	num1 TINYINT UNSIGNED NOT NULL,
	num2 SMALLINT NOT NULL,
	num3 MEDIUMINT DEFAULT '100',
	num4 BIGINT ,
	/* 실수형 */
	fnum1 FLOAT (10,5) NOT NULL,
	fnum2 DOUBLE(20,10)
);
DESC tb_int;

/*
데이터 입력하기
일련번호인 idx 컬럼은 insert문에서 생략하고 작성한다.
자동증가 컬럼으로 지정되어으므로 번호는 자동으로 부여된다.
형식1] insert into 테이블명 (컬럼명) values (값);
*/

INSERT INTO tb_int (num1,num2,num3,num4,fnum1,fnum2)
VALUES (123,12345,1234567,1234567890,12345.12345,1234567890.1234567890);

SELECT * FROM tb_int;
/*
insert문 작성시 컬럼을 명시하지 않으면 
전체 컬럼에 대해 입력값을 작성해야 한다. 
단 이 경우 일련번호가 중복되어 에러가 발생할 수 있으므로 권장하지 않는다!
형식2] insert into 테이블명 values (값);
*/

INSERT INTO tb_int
VALUES(2,123,12345,1234567,1234567890,12345.12345,1234567890.1234567890);

SELECT * FROM tb_int;


/*실습 tb_date 테이블 생성*/

/*
2. 날짜형으로 구성된 테이블

current_timestamp :
	날짜형식으로 지정된 컬럼에 디폴트값으로 
	현재시각을 입력해준다.
	
now() :
	날짜형식으로 지정된 컬럼에 현재시각을 입력할 때
	사용하는 함수로, 초단위까지의 시간이 입력된다.
	오라클의 sysdate와 동일한 역할을 한다.
*/

CREATE TABLE tb_date(
	idx INT PRIMARY KEY AUTO_INCREMENT,
	
	DATE1 DATE NOT NULL,
	DATE2 DATETIME DEFAULT CURRENT_TIMESTAMP 
);
DESC tb_date;

SELECT * FROM tb_date;

# now() 함수를 통해 현재시각 입력
INSERT INTO tb_date (DATE1,DATE2) VALUES('2023-02-25',NOW());
# 쿼리문 작성시 컬럼을 생략하면 default 값이 입력됨.
INSERT INTO tb_date (DATE1) VALUES('2023-02-27');

SELECT * FROM tb_date;
# 실습 ] tb_string 테이블 생성

# 3. 문자형으로 구성된 테이블

/*
VARCHAR(n) :
	문자 타입으로 짧은 글을 저장할때 사용한다.
	(ex. 게시판의 제목)
	
TEXT : 긴 글을 저장할때 사용
	(ex. 게시판의 내용)
*/

CREATE TABLE tb_string (

	idx INT PRIMARY KEY AUTO_INCREMENT,
	
	str1 VARCHAR(30) NOT NULL,
	str2 TEXT
);
DESC tb_string;

SELECT * FROM tb_string;


INSERT INTO tb_string (str1,str2) VALUES('난 짧은글3', '난 엄청 긴글3');

/*
레코드 조회시 조건 추가하기 */

SELECT * FROM tb_string;
SELECT * FROM tb_string WHERE idx=2;
SELECT * FROM tb_string WHERE idx=2 AND str1='난 짧은글2';
SELECT * FROM tb_string WHERE idx=2 AND str1='난 짧은글3';
SELECT * FROM tb_string WHERE idx=2 or str1='난 짧은글3';


/*
레코드 검색시 문자열이 포함된 것을 인출하고 싶다면 like 절을 사용한다. 
*/
# 문자열이 포함된 것을 인출하고 싶다면 like절 사용
SELECT * FROM tb_string WHERE str1 LIKE '%난 짧은%';
SELECT * FROM tb_string WHERE str1 LIKE '난 짧은%';
SELECT * FROM tb_string WHERE str1 LIKE '%난 짧은';


# 실습 tb_spec 테이블 생성

# 4. 특수형

/*
enum : 여러 항목 중 1개만 선택할 수 있는 자료형

set : 여러 항목중 2개 이상을 선택할 수 있는 자료형

오라클의 check 제약조건과 비슷하다 .
*/

CREATE TABLE tb_spec(
	
	idx INT AUTO_INCREMENT,
	
	spec1 ENUM('M','W','T'),
	spec2 SET('A','B','C','D'),
	
	PRIMARY KEY(idx)
);

DESC tb_spec;

# 설정된 값만 추가했으므로 정상입력됨
INSERT INTO  tb_spec (spec1, spec2) VALUES ('W','A,B,C');

#spec1 에러
INSERT INTO  tb_spec (spec1, spec2) VALUES ('X','A,B,C');
#spec2 에러
INSERT INTO  tb_spec (spec1, spec2) VALUES ('M','X,B,C');

INSERT INTO tb_spec (spec2) VALUES('B,C,D');

SELECT * FROM tb_spec;



# DML문 실습

/*
데이터 조작어(Data Manipulation Language)라고 한다. 
데이터베이스에 입력된 레코드를 입력, 조회, 수정, 삭제하기 위한 명령이다.
이와 같은 데이터 처리 작업을 주로 CRUD 라고 한다. 
생성(C) ⇒ Create 는 생성이므로 insert 를 의미한다. 
조회(R) ⇒ Read 혹은 Retrieve는 select 를 의미한다. 
수정(U) ⇒ update를 의미한다.
삭제(D) ⇒ delete를 의미한다. 
*/


# 실습을 위한 테이블 생성

CREATE TABLE board(

	num INT NOT NULL AUTO_INCREMENT,  /* 일련번호, 자동증가 */
	title VARCHAR(100) NOT NULL, /* 제목 : 짧은 텍스트 */
	content TEXT NOT NULL, /* 내용 : 긴 텍스트*/
	id VARCHAR(30) NOT NULL,
	/* 
	작성일 : 
		현재 시각을 디폴트 값으로 설정.*/
	postdate DATETIME DEFAULT CURRENT_TIMESTAMP,
	visitcount MEDIUMINT NOT NULL DEFAULT 0, /* 조회수 */
	PRIMARY KEY (num)
);

INSERT INTO board (title, content, id, visitcount) VALUES 
('첫 번째 게시글입니다.', '안녕하세요. 가입인사 드립니다. 반갑습니다!', 'user01', 0),
('질문이 있습니다.', '데이터베이스 연동 중에 오류가 발생하는데 어떻게 해야 하나요?', 'coder99', 5),
('공지사항 필독 부탁드립니다.', '게시판 이용 규칙을 준수해 주세요. 도배 금지입니다.', 'admin', 120),
('오늘 날씨 정말 좋네요.', '주말에 나들이 가기 딱 좋은 날씨인 것 같아요.', 'flower_like', 3),
('Java 공부 같이 하실 분?', '스터디 그룹 모집합니다. 주 2회 온/오프라인 병행 예정입니다.', 'java_lover', 18),
('마리아DB 테이블 생성 완료!', '연습용 데이터 입력 테스트 중입니다. 잘 들어가는군요.', 'test_user', 1);

SELECT * FROM board;