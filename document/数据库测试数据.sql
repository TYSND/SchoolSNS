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

select avatar,nick,id from userinfo 
where 
nick like '%5%'
and 
(select count(*) from friend where fromid=userinfo.id and toid=1)=0
and
(select count(*) from friend where fromid=1 and toid=userinfo.id)=0
and
id!=1
