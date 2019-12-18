import sys
import socket
import threading
import time
import json
import pymysql
import datetime

class udpServer:
	def __init__(self):
		self.__port=9999
		self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.__sock.bind(('', self.__port))

	def __init__(self,tport):
		self.__port=tport
		self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.__sock.bind(('', self.__port))
		
	def __del__(self):
		self.__sock.close()
		
	def send(self,data,clientIP,clientPort):
		self.__sock.sendto(data.encode("utf-8"),(clientIP,clientPort))
	
	def recv(self,bufsize):
		return self.__sock.recvfrom(bufsize)


class operateDB:
	def __init__(self,host,user,pw,dbname):
		self.__db=pymysql.connect(host,user,pw,dbname)
		self.__cursor=self.__db.cursor()
	def __del__(self):
		self.__db.close()
	
	def select(self,sql):
		try:
			self.__cursor.execute(sql)
			return self.__cursor.fetchall()
		except:
			emptylist=[]
			return emptylist
	def modify(self,sqlList):
		try:
			for sql in sqlList:
				self.__cursor.execute(sql)
			self.__db.commit()
			return 1
		except:
			self.__db.rollback()
			return 0

#import json
#import datetime
#import time
class opJson:
	def __init__(self,jstr,host,port):
		self.__jstr=json.loads(jstr)
		self.__host=host
		self.__port=port
		self.__sendip=[]
		self.__sendport=[]
		self.ores=""
		self.osendip=[]
		self.osendport=[]
	def opt(self):
		ope=self.__jstr['ope']
		print(ope)
		self.__con=operateDB("localhost","root","a46513","schoolsys")
		sql="select funcname from optjson where ope={ope}"
		funcres=self.__con.select(sql.format(ope=ope))
		#for funcrow in funcres:
		#	func=
		func=funcres[0][0]
		res=getattr(self, func)()
		#print(res)
		return res,self.__sendip,self.__sendport
		
	def login(self):
		self.__sendip=[self.__host]
		self.__sendport=[self.__port]
	#得到用户登录使用的账号，密码
		id=self.__jstr['id']
		pw=self.__jstr['pw']
	#查询用户在数据库里的信息
		sql="select id,nick,password,avatar from userinfo where id={id}"
		uinfores=self.__con.select(sql.format(id=id))
		if len(uinfores)==0:
			#登录失败
			jstr={
				"ope":1,
				"status":0,
				"info":"用户不存在"
			}
			json_str = json.dumps(jstr)
			return json_str
		elif  pw!=uinfores[0][2]:
			#登录失败
			jstr={
				"ope":1,
				"status":0,
				"info":"用户名或密码错误"
			}
			json_str = json.dumps(jstr)
			return json_str
		else:
			#登录成功
			#更新用户的ip和port
			sqlList=[]
			sql="update userinfo set ip='{ip}',port='{port}' where id={id}"
			#print(sql.format(ip=self.__host,port=self.__port,id=id))
			sqlList.append(sql.format(ip=self.__host,port=self.__port,id=id))
			self.__con.modify(sqlList)
			#构建回复json串，用字典存储
			jsonDic={}
			#填写个人信息
			jsonDic['ope']=1
			jsonDic['status']=1
			jsonDic['you']={"nick":uinfores[0][1],"avatar":uinfores[0][3],"id":uinfores[0][0]}
			#print(jsonDic)
			
			#查询好友申请信息，填入json串
			friend=[]	#你的好友
			#friendip=[]
			#friendport=[]
			jsonDic['invite']=[]
			#别人对你的申请
			sql="""select a.fromid,a.status,b.nick,b.avatar,b.ip,b.port from 
					(select fromid,status from friend where toid={id}) a
					left join
					(select id,nick,avatar,ip,port from userinfo) b
					on a.fromid=b.id
					"""
			#print(sql.format(id=id))
			otoyres=self.__con.select(sql.format(id=id))# other to you res 
			for otoyrow in otoyres:
				oid=otoyrow[0]
				osta=otoyrow[1]
				onick=otoyrow[2]
				oavatar=otoyrow[3]
				oip=otoyrow[4]
				oport=otoyrow[5]
				tmp={}
				tmp['from']=0
				if oip==None:
					tmp['online']=0
				else:
					tmp['online']=1
				tmp['id']=oid
				#tmp['to']=oid
				tmp['nick']=onick
				tmp['avatar']=oavatar
				tmp['status']=osta
				
				jsonDic['invite'].append(tmp)
				if osta==1:
					friend.append(oid)
					if oip!=None:
						#friendip.append(oip)
						#friendport.append(oport)
						self.osendip.append(oip)
						self.osendport.append(oport)
					
			#你对别人的申请
			sql="""select a.toid,a.status,b.nick,b.avatar,b.ip,b.port from 
					(select toid,status from friend where fromid={id}) a
					left join
					(select id,nick,avatar,ip,port from userinfo) b
					on a.toid=b.id
					"""
			otoyres=self.__con.select(sql.format(id=id))# other to you res 
			for otoyrow in otoyres:
				oid=otoyrow[0]
				osta=otoyrow[1]
				onick=otoyrow[2]
				oavatar=otoyrow[3]
				oip=otoyrow[4]
				oport=otoyrow[5]
				tmp={}
				tmp['from']=1
				if oip==None:
					tmp['online']=0
				else:
					tmp['online']=1
				tmp['id']=oid
				#tmp['to']=oid
				tmp['nick']=onick
				tmp['avatar']=oavatar
				tmp['status']=osta
				jsonDic['invite'].append(tmp)
				if osta==1:
					friend.append(oid)
					if oip!=None:
						#friendip.append(oip)
						#friendport.append(oport)
						self.osendip.append(oip)
						self.osendport.append(oport)
			
			#要给所有好友发送上线通知
			ojsonDic={}
			ojsonDic['ope']=8
			ojsonDic['id']=id
			ojsonDic['online']=1
			self.ores=json.dumps(ojsonDic)
		
			#查询聊天记录，填入json串
			jsonDic['message']=[]
			#每个朋友的聊天记录
			for friendid in friend:
				chatDic={}
				chatDic['id']=friendid
				chatDic['send']=[]
				chatDic['receive']=[]
				sql="""
						select sendtime,content from chathistory
						where
						fromid={id} and toid={fid}
						"""
				sendres=self.__con.select(sql.format(id=id,fid=friendid))# other to you res 
				
				for sendrow in sendres:
					#print(type(sendrow[0]))
					sendtime=time.mktime(sendrow[0].timetuple())
					#print(sendtime)
					content=sendrow[1]
					tmp={}
					tmp['data']=content
					tmp['time']=sendtime
					chatDic['send'].append(tmp)
				sql="""
						select sendtime,content from chathistory
						where
						fromid={fid} and toid={id}
						"""
				recvres=self.__con.select(sql.format(id=id,fid=friendid))# other to you res 
				for recvrow in recvres:
					sendtime=time.mktime(recvrow[0].timetuple())
					content=recvrow[1]
					tmp={}
					tmp['data']=content
					tmp['time']=sendtime
					chatDic['receive'].append(tmp)	
				jsonDic['message'].append(chatDic)
			#将字典转换为json串，并返回
			#print(jsonDic)
			json_str = json.dumps(jsonDic)
			return json_str
		
	
	def register(self):
		self.__sendip=[self.__host]
		self.__sendport=[self.__port]
		#得到用户注册的账号，密码，头像
		id=self.__jstr['id']
		pw=self.__jstr['pw']
		avatar=self.__jstr['avatar']
		nick=self.__jstr['nick']
		#插入数据库
		sqlList=[]
		sql="insert into userinfo values ({id},'{nick}','{pw}',{avatar},null,null)"
		#print(sql.format(ip=self.__host,port=self.__port,id=id))
		sqlList.append(sql.format(id=id,nick=nick,pw=pw,avatar=avatar))
		insertres=self.__con.modify(sqlList)
		#根据操作数据库的结果，构建回复json串
		jsonDic={}
		if insertres==1:	#注册成功
			jsonDic['ope']=2
			jsonDic['status']=1
			jsonDic['info']='register success'
		else:	#注册失败
			jsonDic['ope']=2
			jsonDic['status']=0
			jsonDic['info']='register error,repeated account!'
		json_str = json.dumps(jsonDic)
		return json_str

	def sendmsg(self):
		#得到发送的目的用户，消息内容，发送时间
		myid=self.__jstr['from']
		oid=self.__jstr['to']
		data=self.__jstr['data']
		sendtime=self.__jstr['time']
		ltime=time.localtime(sendtime)
		dt=time.strftime("%Y-%m-%d %H:%M:%S",ltime)
		#查询该用户的ip和端口号，判断是否登录（若ip和端口号为null，则未登录）
		sql="select ip,port from userinfo where id={id}"
		ologres=self.__con.select(sql.format(id=oid))
		oip=ologres[0][0]
		oport=ologres[0][1]
		#根据用户是否登录，设置数据库中该消息的已读未读状态。若登录，则已读（客户端会处理）；若未登录，则未读
		if oip==None:	
			#未登录，仅需要插入数据库
			sqlList=[]
			sql="insert into chathistory values ({myid},{toid},'{dt}','{data}',0)"
			#print(sql.format(myid=myid,toid=oid,dt=dt,data=data))
			#print(sql.format(ip=self.__host,port=self.__port,id=id))
			sqlList.append(sql.format(myid=myid,toid=oid,dt=dt,data=data))
			insertres=self.__con.modify(sqlList)
			jsonDic={}
			json_str = json.dumps(jsonDic)
			return json_str
		else:
			#已登录，插入数据库，并设置发送到的ip和port，构建回复json串
			sqlList=[]
			sql="insert into chathistory values ({myid},{toid},'{dt}','{data}',1)"
			#print(sql.format(ip=self.__host,port=self.__port,id=id))
			sqlList.append(sql.format(myid=myid,toid=oid,dt=dt,data=data))
			insertres=self.__con.modify(sqlList)		
			
			self.__sendip=[oip]
			self.__sendport=[oport]
		
			jsonDic={}
			jsonDic['ope']=3
			jsonDic['from']=myid
			jsonDic['data']=data
			jsonDic['time']=sendtime
			#print(jsonDic)
			json_str = json.dumps(jsonDic)
			return json_str
		
	def setinfo(self):
		#得到用户的个人信息
		id=self.__jstr['id']
		pw=self.__jstr['pw']
		avatar=self.__jstr['avatar']
		nick=self.__jstr['nick']
		#修改数据库
		sqlList=[]
		sql="update userinfo set password='{pw}',avatar={avatar},nick='{nick}' where id={id}"
		#print(sql.format(ip=self.__host,port=self.__port,id=id))
		sqlList.append(sql.format(pw=pw,avatar=avatar,nick=nick,id=id))
		self.__con.modify(sqlList)
		jsonDic={}
		json_str = json.dumps(jsonDic)
		return json_str
		
	def searchfriend(self):
		self.__sendip=[self.__host]
		self.__sendport=[self.__port]
		#得到用户的查询关键字
		data=self.__jstr['data']
		myid=self.__jstr['id']
		jsonDic={}
		jsonDic['ope']=5
		jsonDic['id']={}
		jsonDic['nick']=[]
		#查询数据库，得到账号严格匹配的记录（如果有）
		sql="""
		select avatar,nick,id from userinfo 
		where 
		id={id} 
		and 
		(select count(*) from friend where fromid={id} and toid={myid})=0
		and
		(select count(*) from friend where fromid={myid} and toid={id})=0
		and
		id!={myid}
		"""
		idres=self.__con.select(sql.format(id=data,myid=myid))
		#print(sql.format(id=data,myid=myid))
		if len(idres)==1:
			jsonDic['id']['avatar']=idres[0][0]
			jsonDic['id']['nick']=idres[0][1]
			jsonDic['id']['id']=idres[0][2]
		#查询数据库，得到昵称不严格匹配的记录（如果有）
		sql="""
		select avatar,nick,id from userinfo 
		where 
		nick like '%{data}%'
		and 
		(select count(*) from friend where fromid=userinfo.id and toid={myid})=0
		and
		(select count(*) from friend where fromid={myid} and toid=userinfo.id)=0
		and
		id!={myid}
		"""
		#print(sql.format(data=data,id=data,myid=myid))
		nickres=self.__con.select(sql.format(data=data,id=data,myid=myid))
		for nickrow in nickres:
			tmp={}
			tmp['avatar']=nickrow[0]
			tmp['nick']=nickrow[1]
			tmp['id']=nickrow[2]
			jsonDic['nick'].append(tmp)
		#根据查询结果，构建回复json串
		json_str = json.dumps(jsonDic)
		return json_str
		
	def addfriend(self):
		#得到from和to
		fromid=self.__jstr['from']
		toid=self.__jstr['to']
		
		#修改数据库
		sqlList=[]
		sql="insert into friend values({toid},{fromid},0)"
		#print(sql.format(ip=self.__host,port=self.__port,id=id))
		sqlList.append(sql.format(toid=toid,fromid=fromid))
		self.__con.modify(sqlList)
		
		#得到要加的好友的登录状态
		sql="select ip,port from userinfo where id={toid}"
		ologres=self.__con.select(sql.format(toid=toid))
		oip=ologres[0][0]
		oport=ologres[0][1]
		
		jsonDic={}
		#根据用户是否登录，设置数据库中该消息的已读未读状态。若登录，则已读（客户端会处理）；若未登录，则未读
		if oip==None:	
			json_str = json.dumps(jsonDic)
			return json_str
		else:
			
			self.__sendip=[oip]
			self.__sendport=[oport]
			
			sql="select avatar,nick,id from userinfo where id={fromid}"
			uinfores=self.__con.select(sql.format(fromid=fromid))
			jsonDic['ope']=6
			if len(uinfores)==1:
				jsonDic['from']=fromid
				jsonDic['nick']=uinfores[0][1]
				jsonDic['avatar']=uinfores[0][0]
			json_str = json.dumps(jsonDic)
			return json_str
		
		
	def review(self):
		#得到from，to，和结果
		fromid=self.__jstr['from']
		toid=self.__jstr['to']
		sta=self.__jstr['status']
		#修改数据库
		sqlList=[]
		sql="update friend set status={status} where fromid={fromid} and toid={toid}"
		#print(sql.format(ip=self.__host,port=self.__port,id=id))
		sqlList.append(sql.format(toid=toid,fromid=fromid,status=sta))
		self.__con.modify(sqlList)
		#若申请方客户端在线，则构建回复json串发送
		sql="select ip,port from userinfo where id={fromid}"
		ologres=self.__con.select(sql.format(fromid=fromid))
		oip=ologres[0][0]
		oport=ologres[0][1]
		
		jsonDic={}
		#根据用户是否登录，设置数据库中该消息的已读未读状态。若登录，则已读（客户端会处理）；若未登录，则未读
		if oip==None:	
			json_str = json.dumps(jsonDic)
			return json_str
		else:
			self.__sendip=[oip]
			self.__sendport=[oport]
			jsonDic['ope']=7
			jsonDic['from']=toid
			jsonDic['status']=sta
			json_str = json.dumps(jsonDic)
			return json_str
		
		
	def logout(self):
		#print("logout")
		#得到id
		id=self.__jstr['id']
		#修改数据库中该用户的ip和port为null
		sqlList=[]
		sql="update userinfo set ip=null,port=null where id={id}"
		#print(sql.format(ip=self.__host,port=self.__port,id=id))
		sqlList.append(sql.format(id=id))
		#print(sql)
		self.__con.modify(sqlList)
		#给每个好友发送回复json串
		jsonDic={}
		jsonDic['ope']=8
		jsonDic['id']=id
		jsonDic['online']=0
		sql="select fromid,toid from friend where (toid={id} or fromid={id}) and status=1"
		friendres=self.__con.select(sql.format(id=id))
		for friendrow in friendres:
			if friendrow[0]==id:
				fid=friendrow[1]
			else:
				fid=friendrow[0]
			sql="select ip,port from userinfo where id={id}"
			flogres=self.__con.select(sql.format(id=fid))
			if flogres[0][0]!=None:
				#好友在线，发送离线消息
				self.__sendip.append(flogres[0][0])
				self.__sendport.append(flogres[0][1])
		json_str = json.dumps(jsonDic)
		return json_str		