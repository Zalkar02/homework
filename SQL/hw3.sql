create database hw3 character set utf8 collate utf8_general_ci;

use hw3;

create table marka (id int not null primary key auto_increment, 
	name varchar(255) not null);

create table model (id int not null primary key AUTO_INCREMENT,
	name varchar(255),
	m_id int,
	constraint fk_marka_model_id foreign key (m_id) references marka(id));

insert into marka values(null, "Honda"), (null, "Mersedes");
insert into model values(null,"Adisei", 1),(null, "Partner",1),
	(null, "S", 2),(null, "Rex",2);

select * from marka join model on marka.id = m_id;


create table produser (id int not null primary key auto_increment, 
	name varchar(255) not null);

create table film (id int not null primary key AUTO_INCREMENT,
	name varchar(255),
	p_id int,
	constraint fk_produser_film_id foreign key (p_id) references produser(id));

insert into produser values(null, "Zalkar"), (null, "Nurs");
insert into film values(null,"Film_1", 1),(null, "Film_3",1),
	(null, "Film_2", 2),(null, "Film_4",2);

select * from produser join film on produser.id = p_id;


create table area (id int not null primary key auto_increment, 
	name varchar(255) not null);

create table schools (id int not null primary key AUTO_INCREMENT,
	name varchar(255),
	a_id int,
	constraint fk_area_schools_id foreign key (a_id) references area(id));

insert into area values(null, "№13"), (null, "№9");
insert into schools values(null,"№88", 1),(null, "№56",1),
	(null, "№66", 2),(null, "№12",2);

select * from area join schools on area.id = a_id;