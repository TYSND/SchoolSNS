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
		except:
			self.__db.rollback()