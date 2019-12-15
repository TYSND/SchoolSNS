create table userinfo
(
	id int not null,
	nick varchar(20) not null,
	password varchar(20) not null,
	avatar int not null,
	ip varchar(50),
	port int,
	primary key(id)
);

create table friend
(
	toid int not null,
	fromid int not null,
	status int not null,
	primary key(toid,fromid)
);

create table chathistory
(
	fromid int not null,
	toid int not null,
	sendtime datetime not null,
	content varchar(200) not null,
	readed tinyint not null,
	primary key(fromid,toid,sendtime)
);

create table optjson
(
	ope int not null,
	funcname varchar(20) not null,
	primary key (ope)
);
