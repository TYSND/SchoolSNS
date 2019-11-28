create table userinfo
(
	id int not null,
	nick varchar(20) not null,
	password varchar(20) not null,
	primary key(account)
);

create table friend
(
	toid int not null,
	fromid int not null,
	stat int not null,
	primary key(toaccount,fromaccount)
);

create table chathistory
(
	fromid int not null,
	toid int not null,
	sendtime datetime not null,
	content varchar(200) not null,
	contenttype int not null,
	primary key(fromid,toid,sendtime)
);
