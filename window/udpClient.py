class udpClientsock:
	def __init__(self):
		self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		
	def __del__(self):
		self.__sock.close()
		
	def send(self,data):
		self.__sock.sendto(data.encode("utf-8"),("203.195.198.41",9527))
	
	def recv(self,bufsize):
		return self.__sock.recvfrom(bufsize)

#处理json串的线程类
class handelJson (threading.Thread):
	def __init__(self, threadID, name,data):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.__jstr=data
	def run(self):
		optjson=opJson(jstr)
		optjson.opt()

#接收服务器消息的线程类，堵塞，接收到json串后，开线程，handelJson类处理
class recvThread(threading.Thread):
	def __init__(self,ucs):
		self.ucs=ucs
	def run(self):
		cnt=1
		threads=[]
		while True:
			recvData=self.ucs.recv(4096)
			jstr=recvData[0].decode("utf-8")
			#optjson=opJson(jstr)
			t=handelJson(cnt,cnt,jstr)
			threads.append(t)
			threads[cnt-1].start()
			cnt+=1


#发送数据到服务器的线程类，接收到其他窗口的json串后，开这个类对应的线程，send数据到服务器
class sendThread(threading.Thread):
	def __init__(self,ucs,data):
		#这里的data就是string，不用encode成byte数组
		self.ucs=ucs
		self.__data=data
	def run(self):
		self.ucs.send(data)
		
'''
class clientRun:
	def __init__(self):
		self.__ucs=udpClientsock()
	def run(self):
		cnt=1
		threads=[]
		while True:
			recvData=self.__ucs.recv(4096)
			jstr=recvData[0].decode("utf-8")
			#optjson=opJson(jstr)
			t=handelJson(cnt,cnt,jstr)
			threads.append(t)
			threads[cnt-1].start()
			cnt+=1
	def send(self,data):
		self.__ucs.send(data.encode("utf-8"))
'''

#import json
class opJson:
	def __init__(self,jstr):
		self.__jstr=json.loads(jstr)
		self.__opeFunc=["login","register","sendmsg","searchfriend","addfriend","review","logout"]
	def opt(self):
		ope=self.__jstr['ope']
		
		func=self.__opeFunc[ope-1]
		res=getattr(self, func)()
		#print(res)
		
	def login(self):
		global h
		h.loginCallback(self.__jstr)
	
	def register(self):
		global h
		h.registerCallback(self.__jstr)

	def sendmsg(self):
		pass
		
	def setinfo(self):
		pass
		
	def searchfriend(self):
		pass

		
	def addfriend(self):
		pass
		
		
	def review(self):
		pass
		
		
	def logout(self):
		pass