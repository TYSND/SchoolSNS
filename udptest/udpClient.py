class udpClient:
	def __init__(self):
		self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		
	def __del__(self):
		self.__sock.close()
		
	def send(self,data,clientIP,clientPort):
		self.__sock.sendto(data.encode("utf-8"),(clientIP,clientPort))
	
	def recv(self,bufsize):
		return self.__sock.recvfrom(bufsize)