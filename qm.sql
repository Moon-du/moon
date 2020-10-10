#练习一
#1、在数据库中定义如下数据表并在表中插入相应的数据
#图书信息表(总编号z_no,分类号f_no,书名b_name,出版单位b_dw,单价b_price,作者b_writer)
#读者信息表(借书证号r_no,单位r_dw,姓名r_name,性别r_sex,职称r_job,地址r_addr)
#借阅信息表(借书证号r_no,总编号z_no,借书日期b_date)

CREATE DATABASE test;
USE test;

CREATE TABLE book (
	z_no VARCHAR ( 20 ) PRIMARY KEY COMMENT "总编号",
	f_no VARCHAR ( 20 ) UNIQUE NOT NULL COMMENT "分类号",
	b_name VARCHAR ( 20 ) NOT NULL COMMENT "书名",
	b_dw VARCHAR ( 20 ) NOT NULL COMMENT "出版单位",
	b_price INT NOT NULL COMMENT "单价",
	b_writer VARCHAR ( 20 ) NOT NULL COMMENT "作者" 
);

CREATE TABLE rbook (
	r_no VARCHAR ( 20 ) PRIMARY KEY COMMENT "借书证号",
	r_dw VARCHAR ( 20 ) NOT NULL COMMENT "单位",
	r_name VARCHAR ( 20 ) NOT NULL COMMENT "姓名",
	r_sex enum ( "男", "女", "未知" ) DEFAULT "未知" NOT NULL COMMENT "性别",
	r_job VARCHAR ( 20 ) NOT NULL COMMENT "职称",
	r_addr VARCHAR ( 20 ) NOT NULL COMMENT "地址" 
);

CREATE TABLE lbook (
	r_no VARCHAR ( 20 ) PRIMARY KEY COMMENT "借书证号",
	z_no VARCHAR ( 20 ) UNIQUE COMMENT "总编号",
	b_date DATE COMMENT "借书日期",
	FOREIGN KEY ( z_no ) REFERENCES book ( z_no ) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY ( r_no ) REFERENCES rbook ( r_no ) ON DELETE CASCADE ON UPDATE CASCADE 
);

delimiter //
CREATE PROCEDURE inster_y ( IN y INT ) BEGIN
	DECLARE
		x INT DEFAULT 1;
	WHILE
			x <= y DO
			INSERT INTO book
		VALUES
			( CONCAT( "Z_", x ), CONCAT( "F_", x ), "书名", "单位", 100, "作者" );
		SELECT
			z_no INTO @Z 
		FROM
			book 
		WHERE
			z_no = CONCAT( "Z_", x );
		INSERT INTO rbook
		VALUES
			( CONCAT( "R_", @z ), "单位", "姓名", "男", "职员", "地址" );
		SELECT
			r_no INTO @R 
		FROM
			rbook 
		WHERE
			r_no = CONCAT( "R_", @z );
		INSERT INTO lbook
		VALUES
			(
				@R,
				@Z,
			CURDATE());
		
		SET x = x + 1;
		
	END WHILE;
	
END // 

DROP PROCEDURE inster_y;
CALL inster_y ( 10 );

TRUNCATE book;
TRUNCATE lbook;
TRUNCATE rbook;

#2、查询出作者姓"李"的所有图书信息

SELECT
	* 
FROM
	book 
WHERE
	b_writer LIKE "李%";
	
#3、查询出书名包含"数据库"并且单价不高于20元的所有图书信息

SELECT
	* 
FROM
	book 
WHERE
	b_name LIKE "%数据库%" 
	AND b_price <= 20;
	
#4、查询出"高等教育出版社"出版的图书中最高价、最低价和平均价

SELECT
	b_dw 出版社,
	MAX( b_price ) 最高价,
	MIN( b_price ) 最低价,
	AVG( b_price ) 平均价 
FROM
	book 
WHERE
	b_dw = "高等教育出版社";
	
#5、按分类号降序显示各种图书的分类号、书名和作者

SELECT
	f_no 分类号,
	b_name 书名,
	b_writer 作者 
FROM
	book 
ORDER BY
	f_no DESC;
	
#6、按分类号升序显示"清华大学出版社"和"北京大学出版社"出版的所有图书

SELECT
	* 
FROM
	book 
WHERE
	b_dw IN ( "清华大学出版社", "北京大学出版社" ) 
ORDER BY
	f_no;
	
#7、统计出单价在50到100之间的图书数量

SELECT
	COUNT( 1 ) 
FROM
	book 
WHERE
	b_price BETWEEN 50 
	AND 100;
	
#8、分组统计出2000年前借阅过，并且借阅数量不低于3本的借书证号和借阅数量

SELECT
	r.r_no 借阅证号,
	COUNT( 1 )借阅数量 
FROM
	rbook r
	NATURAL JOIN lbook l 
WHERE
	l.b_date < "2020-01-01" GROUP BY r.r_no HAVING COUNT( 1 ) >= 3;
	
#9、分组统计出各单位借阅图书的数量

SELECT
	r.r_dw 单位,
	COUNT( 1 ) 数量 
FROM
	rbook r
	NATURAL JOIN lbook 
GROUP BY
	r.r_dw;
	
	
#练习二
#1、在数据库中定义如下数据表并在表中插入相应数据
#学生信息表(学号s_no,姓名s_name,年龄s_age,性别s_sex,所在系s_dept)
#课程信息表(课程号c_no,课程名c_name,先行课c_before,学分credit)
#成绩信息表(学号s_no,课程号c_no,成绩score)

CREATE TABLE student (
	s_no INT PRIMARY KEY COMMENT "学号",
	s_name VARCHAR ( 20 ) NOT NULL COMMENT "姓名",
	s_age INT NOT NULL COMMENT "年龄",
	s_sex enum ( "男", "女", "未知" ) DEFAULT "未知" COMMENT "性别",
	s_dept VARCHAR ( 20 ) NOT NULL COMMENT "院系" 
);

CREATE TABLE course (
	c_no VARCHAR ( 20 ) NOT NULL COMMENT "课程号",
	c_name VARCHAR ( 20 ) NOT NULL COMMENT "课程名",
	c_before VARCHAR ( 20 ) COMMENT "前置课",
	credit INT COMMENT "学分" 
);

CREATE TABLE score (
	s_no INT NOT NULL COMMENT "学号",
	c_no VARCHAR ( 20 ) NOT NULL COMMENT "课程号",
	score INT NOT NULL COMMENT "成绩" 
);

delimiter //
CREATE PROCEDURE inster_y ( IN y INT ) BEGIN
	DECLARE
		x INT DEFAULT 1;
	WHILE
			x <= y DO
			INSERT INTO student
		VALUES
			( x, "姓名", 18, "男", "计算机系" );
		SELECT
			s_no INTO @S 
		FROM
			student 
		WHERE
			s_no = x;
		INSERT INTO course
		VALUES
			( CONCAT( "C_", x ), "课程名", "前置课", 20 );
		SELECT
			c_no INTO @C 
		FROM
			course 
		WHERE
			c_no = CONCAT( "C_", x );
		INSERT INTO score
		VALUES
			( @S, @C, 100 );
		
		SET x = x + 1;
		
	END WHILE;
	
END // 

DROP PROCEDURE inster_y;
CALL inster_y ( 10 );


#2、查询姓"刘"的同学的学号和姓名

SELECT
	s_no 学号,
	s_name 姓名 
FROM
	student 
WHERE
	s_name LIKE "刘%";
	
#3、查询"数据库原理"课程的课程号和学分

SELECT
	c_name 课程名,
	c_no 课程号,
	credit 学分 
FROM
	course 
WHERE
	c_name = "数据库原理";
	
#4、查询没有学过"数据库原理"的学生姓名和学号

SELECT
	* 
FROM
	student st
	NATURAL JOIN score sc 
WHERE
	sc.c_no != ( SELECT c_no FROM course WHERE c_name = "数据库原理" );
	
#5、查询学过"数据库原理"先行课的学生学号

SELECT
	s.s_no 学号 
FROM
	course c
	NATURAL JOIN score s 
WHERE
	c.c_before = ( SELECT c_before FROM course WHERE c_name = "数据库原理" );
	
#6、查询"计算机系"所有学生的平均年龄

SELECT
	s_dept 院系,
	AVG( s_age ) 平均年龄 
FROM
	student 
WHERE
	s_dept = "计算机系" 
GROUP BY
	s_dept;
	
#7、查询"计算机系"男、女学生的平均年龄

SELECT
	s_dept 院系,
	s_sex 性别,
	AVG( s_age ) 平均年龄 
FROM
	student 
WHERE
	s_dept = "计算机系" 
GROUP BY
	s_sex;
	
#8、查询比"计算机系"所有年龄都小的其他系学生

SELECT
	* 
FROM
	student 
WHERE
	s_age < ALL ( SELECT s_age 年龄 FROM student WHERE s_dept = "计算机系" ); 
AND s_dept != "计算机系";
	
#9、查询至少比"计算机系"中1名学生年龄大的其他系学生信息

SELECT 
* 
FROM 
	student 
WHERE 
	s_age > ANY ( SELECT s_age 年龄 FROM student WHERE s_dept = "计算机系" ) 
AND s_dept != "计算机系";

#10、查询"计算机系"没有成绩信息的学生

SELECT
	* 
FROM
	student s
	LEFT JOIN score s1 ON s.s_no = s1.s_no 
WHERE
	s_dept = "计算机系" 
	AND ISNULL( s1.score );
	
#11、查询"计算机系"参加了考试的学生数据库这门课的平均成绩


SELECT
	AVG( s1.score ) 平均成绩	
FROM
	student s
	JOIN score s1 ON s.s_no = s1.s_no
	JOIN course c ON s1.c_no = c.c_no 
WHERE
	s_dept = "计算机系" 
	AND c.c_name = "数据库原理";
	
#12、查询"计算机系"参加了考试的学生数据库这门课的最高分、最低分

SELECT
	max( s1.score ) 最高分,
	min( s1.score ) 最低分 
FROM
	student s
	JOIN score s1 ON s.s_no = s1.s_no
	JOIN course c ON s1.c_no = c.c_no 
WHERE
	s_dept = "计算机系" 
	AND c.c_name = "数据库原理"

#练习三
#1、在数据库中定义如下数据表并在表中插入相应数据
#学生信息表(学号s_no,姓名s_name,性别s_sex,专业s_dept,出生年月s_date)
#教师信息表(教师编号t_no,姓名t_name,所在部门t_dept,职称t_job)
#授课信息表(教师编号t_no,学号s_no,课程编号c_no,课程名称c_name,教材book,学分credit,成绩score)

CREATE TABLE student1 (
	s_no VARCHAR(20) PRIMARY KEY COMMENT "学号",
	s_name VARCHAR ( 20 ) NOT NULL COMMENT "姓名",
	s_sex enum ( "男", "女", "未知" ) DEFAULT "未知" NOT NULL COMMENT "性别",
	s_dept VARCHAR ( 20 ) NOT NULL COMMENT "专业",
	s_date date NOT NULL COMMENT "出生年月"
);

CREATE TABLE teacher(
	t_no VARCHAR(20) PRIMARY KEY COMMENT "教师编号",
	t_name VARCHAR ( 20 ) NOT NULL COMMENT "姓名",
	t_dept VARCHAR ( 20 ) NOT NULL COMMENT "所在部门",
	t_job VARCHAR ( 20 ) NOT NULL COMMENT "职称"
);

CREATE TABLE course1(
	t_no VARCHAR(20) NOT NULL COMMENT "教师编号",
	s_no VARCHAR(20) NOT NULL COMMENT "学号",
	c_no  VARCHAR(20) NOT NULL COMMENT "课程编号",
	c_name VARCHAR ( 20 ) NOT NULL COMMENT "课程名称",
	book VARCHAR ( 20 ) NOT NULL COMMENT "教材",
	credit INT NOT NULL COMMENT "学分",
	score INT NOT NULL COMMENT "成绩"
);

delimiter //
CREATE PROCEDURE inster_y ( IN y INT ) BEGIN
	DECLARE
		x INT DEFAULT 1;
	WHILE
			x <= y DO
			INSERT INTO student1
		VALUES
			( x, "姓名", "男", "计算机系" ,CURDATE());
		SELECT
			s_no INTO @S 
		FROM
			student1 
		WHERE
			s_no = x;
		INSERT INTO teacher
		VALUES
			( CONCAT( "T_", x ), "姓名", "教务处", "教导主任");
		SELECT
			t_no INTO @T
		FROM
			teacher 
		WHERE
			t_no = CONCAT( "T_", x );
		INSERT INTO course1
		VALUES
			(@T, @S,CONCAT( "C_", x ),"计算机","C++",20,100);
		
		SET x = x + 1;
		
	END WHILE;
	
END // 

DROP PROCEDURE inster_y;
CALL inster_y ( 10 );

#2、查询学习过"数据库"课程且成绩不及格的学生学号和任课老师编号

SELECT
	t_no 教师编号,
	s_no 学生编号 
FROM
	course1 
WHERE
	c_name = "数据库" 
	AND score < 60;

#3、查询学习过"英语"课程的"计算机系"学生学号、姓名和成绩

SELECT
	s.s_no 学号,
	s.s_name 姓名,
	c.score 成绩 
FROM
	student1 s
	NATURAL JOIN course1 c 
WHERE
	s.s_dept = "计算机系" 
	AND c.c_name = "英语"
	
#4、查询教师"张三"所教过的并且成绩在90分以上的学生学号、姓名和专业

SELECT 
	s.s_no 学号, s.s_name 姓名, s.s_dept 专业 
FROM 
	student1 s NATURAL JOIN course1 c 
WHERE c.score > 90
AND c.t_no in(
	SELECT
		t_no 
	FROM
		teacher 
	WHERE
	t_name = "张三")

#5、删除学生表中学号为"201701010001"的记录
DELETE 
FROM
	student1 
WHERE
	s_no = 201701011001;

#6、将教师"张三"的所在部门修改为"计算机"

UPDATE teacher 
SET t_dept = "计算机" 
WHERE
	t_name = "张三";

#7、建立"计算机系"有过不及格成绩的学生视图

CREATE VIEW nj AS SELECT
* 
FROM
	student1 s
	NATURAL JOIN course1 c 
WHERE
	s.s_dept = "计算机系" 
	AND c.score < 60;

SELECT * FROM nj;


#练习四
#1、在数据库中定义如下数据表并在表中插入相应数据
#职工信息表(职工号e_no,姓名e_name,性别e_sex,职务e_job,家庭地址e_addr,部门编号d_no)
#部门信息表(部门编号d_no,部门名称d_name,地址d_addr,电话d_number)
#健康信息表(职工号e_no,检查身体日期c_date,健康状况e_state)

CREATE TABLE emp(
	e_no VARCHAR(20) PRIMARY KEY COMMENT "职工号",
	e_name VARCHAR ( 20 ) NOT NULL COMMENT "姓名",
	e_sex enum ( "男", "女", "未知" ) DEFAULT "未知" NOT NULL COMMENT "性别",
	e_job VARCHAR ( 20 ) NOT NULL COMMENT "职务",
	e_addr VARCHAR ( 20 ) NOT NULL COMMENT "家庭住址",
	d_no VARCHAR ( 20 ) NOT NULL COMMENT "部门编号"
);

CREATE TABLE dept(
	d_no VARCHAR(20) PRIMARY KEY COMMENT "部门编号",
	d_name VARCHAR ( 20 ) NOT NULL COMMENT "部门名称",
	d_addr VARCHAR ( 20 ) NOT NULL COMMENT "地址",
	d_number INT NOT NULL COMMENT "电话"
);

CREATE TABLE health(
	e_no VARCHAR(20) PRIMARY KEY COMMENT "职工号",
	c_date date NOT NULL COMMENT "检查身体日期",
	e_state VARCHAR(20) NOT NULL COMMENT "健康状况"
);

delimiter //
CREATE PROCEDURE inster_y ( IN y INT ) BEGIN
	DECLARE
		x INT DEFAULT 1;
	WHILE
			x <= y DO
			INSERT INTO emp
		VALUES
			( x,"姓名","男","职员","地址",CONCAT("D_",x));
		SELECT
			d_no INTO @D 
		FROM
			emp 
		WHERE
			e_no = x;
		INSERT INTO dept
		VALUES
			(@D,"部门名称","地址",11000);
		SELECT
			e_no INTO @E
		FROM
			emp 
		WHERE
			e_no = x;
		INSERT INTO health
		VALUES
			(@E, CURDATE(),"健康");
		
		SET x = x + 1;	
	END WHILE;
END // 

DROP PROCEDURE inster_y;
CALL inster_y ( 10 );

#2、查询所有"女科长"的详细信息

SELECT * FROM emp WHERE e_job = "科长" AND e_sex = "女";

#3、查询"财务部"的科长姓名和家庭地址

SELECT
	d.d_name 部门名称,
	e.e_name 姓名,
	e.e_addr 家庭住址 
FROM
	emp e
	NATURAL JOIN dept d 
WHERE
	e.e_job = "科长" 
	AND d.d_name = "财务部";

#4、查询"财务部"健康状况为"良好"的职工姓名和家庭地址

SELECT
	d.d_name 部门名称,
	e.e_name 姓名,
	e.e_addr 家庭住址 
FROM
	emp e
	NATURAL JOIN dept d 
	NATURAL JOIN health h
WHERE
	h.e_state = "良好" 
	AND d.d_name = "财务部";

#5、查询最近一年没有体检过的职工工号、姓名和职务

SELECT
	e.e_no 职工号,
	e.e_name 姓名,
	e.e_job 职务
FROM
	emp e
	NATURAL JOIN health h
WHERE
	TIMESTAMPDIFF(year,h.c_date,CURDATE()) > 1;
	
	
#6、删除职工关系表中职工号为"e001"的记录

DELETE FROM emp WHERE e_no = "e001";

#7、将职工"e002"的健康状态改为"一般"

UPDATE health SET e_state = "一般" WHERE e_no = "e002"

#8、向健康信息表中增加一个"备注"列，数据类型为字符串，长度为20

ALTER TABLE health ADD notes VARCHAR ( 20 ) COMMENT "备注";



#练习五
#1、在数据库中定义如下数据表并在表中插入相应数据
#供应商信息表(供应商代码s_no,姓名s_name,所在城市s_city,练习电话s_phone)
#工程信息表(工程代码p_no,工程名p_name,负责人p_leader,预算p_budget)
#零件信息表(零件代码c_no,零件名c_name,规格c_standard,产地c_city,颜色c_color)
#供应信息表(供应商代码s_no,工程代码p_no,零件代码c_no,数量)

CREATE TABLE supplier(
	s_no VARCHAR(20) PRIMARY KEY COMMENT "供应商代码",
	s_name VARCHAR ( 20 ) NOT NULL COMMENT "姓名",
	s_city VARCHAR ( 20 ) NOT NULL COMMENT "所在城市",
	s_phone INT NOT NULL COMMENT "电话"
);

CREATE TABLE project(
	p_no VARCHAR(20) PRIMARY KEY COMMENT "工程代码",
	p_name VARCHAR ( 20 ) NOT NULL COMMENT "工程名",
	p_leader VARCHAR ( 20 ) NOT NULL COMMENT "负责人",
	p_budget INT NOT NULL COMMENT "预算"
);

CREATE TABLE part(
	c_no VARCHAR(20) PRIMARY KEY COMMENT "零件代码",
	c_name VARCHAR ( 20 ) NOT NULL COMMENT "零件名",
	c_standard VARCHAR ( 20 ) NOT NULL COMMENT "规格",
	c_city VARCHAR ( 20 ) NOT NULL COMMENT "产地",
	c_color VARCHAR ( 20 ) NOT NULL COMMENT "颜色"
);

CREATE TABLE supply(
	s_no VARCHAR(20) PRIMARY KEY COMMENT "供应商代码",
	p_no VARCHAR ( 20 ) NOT NULL COMMENT "工程代码",
	c_no VARCHAR ( 20 ) NOT NULL COMMENT "零件代码",
	c_num INT NOT NULL COMMENT "数量"
);


delimiter //
CREATE PROCEDURE inster_y ( IN y INT ) BEGIN
	DECLARE
		x INT DEFAULT 1;
	WHILE
			x <= y DO
			INSERT INTO supplier
		VALUES
			( CONCAT("S_",x), "姓名", "城市", 110);
		SELECT
			s_no INTO @S 
		FROM
			supplier 
		WHERE
			s_no = CONCAT("S_",x);
		INSERT INTO project
		VALUES
			( CONCAT( "P_", x ), "工程名", "负责人", 100);
		SELECT
			p_no INTO @P
		FROM
			project 
		WHERE
			p_no = CONCAT( "P_", x );
		INSERT INTO part
		VALUES
			(CONCAT( "C_", x ), "零件名", "规格","产地","颜色");
		SELECT
			c_no INTO @C
		FROM
			part 
		WHERE
			c_no = CONCAT("C_",x);
		INSERT INTO supply
		VALUES
			( @S,@P,@C, 100);
		
		SET x = x + 1;
		
	END WHILE;
	
END // 

DROP PROCEDURE inster_y;
CALL inster_y ( 10 );

#2、查询"成都"供应商的姓名和电话

SELECT
	s_name 姓名,
	s_phone 电话,
	s_city 城市 
FROM
	supplier 
WHERE
	s_city = "成都";
	
#3、查询预算在50000~100000之间的工程信息，并将结果按预算降序排列

SELECT
	* 
FROM
	project 
WHERE
	p_budget BETWEEN 50000 
	AND 100000;
	
#4、查询使用供应商"s1"所供应零件的工程代码

SELECT
	p_no 
FROM
	supply 
WHERE
	s_no = ( SELECT s_no FROM supplier WHERE s_name = "S1" );
	
#5、查询工程项目"p2"使用的各种零件名称和数量

SELECT
	p.c_name 零件名称,
	s.c_num 零件数量
FROM
	supply s NATURAL JOIN part p 
WHERE
	p_no = ( SELECT p_no FROM project WHERE p_name = "p2" );
	
#6、查询"上海"供应商提供的所有零件号码

SELECT
	s.s_city 城市,
	p.c_no 零件号码 
FROM
	supplier s
	NATURAL JOIN supply s1
	NATURAL JOIN part p 
WHERE
	s.s_city = "上海"
	
#7、查询使用"上海"生成的零件的工程名称

SELECT
	p_name 
FROM
	project 
WHERE
	p_no =(
	SELECT
		p_no 
	FROM
		supply s
		NATURAL JOIN part p 
	WHERE
		p.c_city = "上海" 
	)

#8、查询没有使用"天津"生成的零件的工程名称

SELECT
	p_name 
FROM
	project 
WHERE
	p_no NOT IN(
	SELECT
		p_no 
	FROM
		supply s
		NATURAL JOIN part p 
	WHERE
		p.c_city = "天津" 
	)

SELECT	* FROM supplier;
SELECT * FROM project;
SELECT * FROM part;
SELECT * FROM supply;

#9、查询"p1"工程项目中"成都"供应商供应的所有零件数量（按照零件类型分组统计）、

SELECT
	s1.c_no 零件类型,
	s1.c_num 零件数量 
FROM
	supplier s
	NATURAL JOIN supply s1 
	NATURAL JOIN project p
WHERE
	p.p_name = "P1" 
	AND s.s_city = "成都" ;

#10、查询"p1"工程项目中没有使用哪些供应商提供的零件

SELECT
	s_name 
FROM
	supplier 
WHERE
	s_name NOT IN (
	SELECT
		s.s_name 
	FROM
		supplier s
		NATURAL JOIN supply s1
		NATURAL JOIN project p 
	WHERE
		p.p_name = "P1" 
	);

