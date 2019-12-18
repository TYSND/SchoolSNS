import sys
import socket
import threading
import time
import json
import pymysql
import datetime
from udpServer import udpServer,operateDB,opJson
'''
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
'''
	
us=udpServer(9527)

'''
class recvThread (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		global flag,remoteHost,remotePort,us
		#us=udpServer(9527)
		while True:
			recvData, (remoteHost, remotePort)=us.recv(1024)
			print("recv:%s"%recvData)
			print("[%s:%s] connect" % (remoteHost, remotePort))
			flag=1
'''
class sendThread (threading.Thread):
	def __init__(self, threadID, name,data, host,port):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.__data=data
		self.__host =host
		self.__port=port
	def run(self):
		global us
		opj=opJson(self.__data,self.__host,self.__port)
		res,toiplst,toportlst=opj.opt()
		#restr=json.loads(res)
		#print(restr)
		print(toiplst)
		print(toportlst)
		cnt=0
		while cnt<len(toiplst):
			us.send(res,toiplst[cnt],toportlst[cnt])
			cnt+=1
		cnt=0
		while cnt<len(opj.osendip):
			us.send(opj.ores,opj.osendip[cnt],opj.osendport[cnt])
			cnt+=1
		#us.send(line,self.__host,int(self.__port))
		#time.sleep(1)

'''
class UdpServer1(object):
	def udpServer(self):
		thread1 = sendThread(1, "Thread-1", 1)
		thread2 = recvThread(2, "Thread-2", 2)

		thread1.start()
		thread2.start()
		thread1.join()
		thread2.join()
'''
		
	
            
if __name__ == "__main__":
	cnt=1
	threads=[]
	while True:
		recvData, (remoteHost, remotePort)=us.recv(1024)
		#print("recv:%s"%recvData)
		print("[%s:%s] connect" % (remoteHost, remotePort))
		t=sendThread(cnt,cnt,recvData,remoteHost,remotePort)
		threads.append(t)
		#threads[cnt-1].setDaemon(True)#声明t为守护线程，设置的话，子线程将和主线程一起运行，并且直接结束，不会再执行循环里面的子线程
		threads[cnt-1].start()
		cnt+=1
