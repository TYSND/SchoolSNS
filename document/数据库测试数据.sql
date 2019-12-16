insert into userinfo
(id,nick,password,avatar)
values
(1,"user1","123",1);

insert into userinfo
(id,nick,password,avatar)
values
(2,"user2","123",1);

insert into userinfo
(id,nick,password,avatar)
values
(3,"user3","123",1);

insert into userinfo
(id,nick,password,avatar)
values
(5,"user5","123",1);

insert into userinfo
(id,nick,password,avatar)
values
(6,"user56","123",1);

insert into userinfo
(id,nick,password,avatar)
values
(4,"user4","123",1);

insert into friend
values
(2,1,1);

insert into friend
values
(1,3,1);

insert into friend
values
(4,1,0);

insert into chathistory
values
(1,2,"2019-10-10 12:11:23","hi,2",1);

insert into chathistory
values
(1,3,"2019-11-10 14:11:23","hi,3",1);

insert into chathistory
values
(3,1,"2019-11-11 2:11:23","hello,1",0);

insert into chathistory
values
(2,1,"2019-10-23 4:12:23","hehe",1);

{
	'ope': 1, 
	'status': 1, 
	'you': 
	{
		'nick': 'user1', 'avatar': 1, 'id': 1
	}, 
	'invite': 
	[
		{'from': 1, 'to': 3, 'nick': 'user3', 'avatar': 1, 'status': 1},
		{'from': 2, 'to': 1, 'nick': 'user2', 'avatar': 1, 'status': 1},
		{'from': 4, 'to': 1, 'nick': 'user4', 'avatar': 1, 'status': 0}
	]
	, 
	'message': 
	[
		{
			'id': 3, 
			'send': 
			[
				{'data': 'hi,3', 'time': datetime.datetime(2019, 11, 10, 14, 11, 23)}
			], 
			'receive': 
			[
				{'data': 'hello,1', 'time': datetime.datetime(2019, 11, 11, 2, 11, 23)}
			]
		}, 
		{
			'id': 2, 
			'send': 
			[
				{'data': 'hi,2', 'time': datetime.datetime(2019, 10, 10, 12, 11, 23)}
			], 
			'receive': 
			[
				{'data': 'hehe', 'time': datetime.datetime(2019, 10, 23, 4, 12, 23)}
			]
		}
	]
}