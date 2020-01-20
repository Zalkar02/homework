create database hw4 character set utf8 collate utf8_general_ci;

use hw4;

create table interest(id int NOT NULL PRIMARY KEY AUTO_INCREMENT, 
	name varchar(20) not null);

create table doctors(id int not null primary key AUTO_INCREMENT, 
	name varchar(20) not null);

create table interest_doctors (id int not null primary key AUTO_INCREMENT,
	id_i int, id_d int,
	constraint fk_int_doc foreign key(id_i) references interest(id),
	constraint fk_doc_int foreign key(id_d) references doctors(id));

insert into interest values(null, "Maks"), (null, "Samat"), (null, "Alex");
insert into doctors values(null, "Lor"), (null, "Okulist"), (null, "Pediator");
insert into interest_doctors values(null, 1, 2), (null,2,2), (null,3,2), (null, 2,1),
	(null, 3, 1), (NULL, 3,3),(NULL, 2,3),(null,1,3);	

select interest_doctors.id, interest.name, doctors.name
from interest join interest_doctors on interest_doctors.id_i = interest.id 
join doctors on interest_doctors.id_d = doctors.id;


-- многие ко многим employees, dept_manager, departments
-- один ко многим employees, titles

create table students (id int not null primary key auto_increment,
	name varchar(20));
create table courses (id int not null primary key auto_increment,
	name varchar(50));
create table students_courses (id int not null primary key AUTO_INCREMENT,
	id_s int, id_c int,
	constraint fk_stud_course foreign key(id_s) references students(id),
	constraint fk_course_stud foreign key(id_c) references courses(id));

insert into students values(null, "Stela"), (Null, "Eldiyar"), (null, "Syrgak"), 
	(null, "Nurs"), (null, "Adyl");
insert into courses values(null, "Python"), (null, "Front-end");
insert into students_courses values(null, 1,1), (null, 1,2), (null, 2,1), (null, 3,1),(null,4,2),(null,5,2);


select students_courses.id, students.name as student, courses.name as course from students_courses
join students on students.id = id_s join courses on courses.id = id_c; 