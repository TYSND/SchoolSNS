import sys
#reload(sys)
#	sys.setdefaultencoding('utf-8')
 
import socket
 
class UdpClient(object):
    def tcpclient(self):
        clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #while True:
        line=input()
        #line="hehe"
        sendDataLen = clientSock.sendto(line.encode(), ('203.195.198.41', 9527))
        #recvData = clientSock.recvfrom(1024)
        print ("sendDataLen: ", sendDataLen)
        #print ("recvData: ", recvData)
        
        #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #sock.bind(('153.3.61.194', 9527))
        #while True:
        recvData1 = clientSock.recvfrom(1024)
            #print ("sendDataLen: ", sendDataLen)
        print ("recvData: ", recvData1)
		
        line=input()
        #line="hehe"
        sendDataLen = clientSock.sendto(line.encode(), ('45.32.65.53', 9527))
        #recvData = clientSock.recvfrom(1024)
        print ("sendDataLen: ", sendDataLen)
        #print ("recvData: ", recvData)
        
        #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #sock.bind(('153.3.61.194', 9527))
        #while True:
        recvData1 = clientSock.recvfrom(1024)
            #print ("sendDataLen: ", sendDataLen)
        print ("recvData: ", recvData1)		
        recvData2 = clientSock.recvfrom(1024)
            #print ("sendDataLen: ", sendDataLen)
        print ("recvData: ", recvData2)
        line="connect"
        sendDataLen = clientSock.sendto(line.encode(), (recvData1[0],int(recvData2[0])))
        while True:		
            recvData3 = clientSock.recvfrom(1024)
            print ("recvData: ", recvData3)
            line=input()
            sendDataLen = clientSock.sendto(line.encode(), (recvData1[0],int(recvData2[0])))
        clientSock.close()
        
if __name__ == "__main__":
    udpClient = UdpClient()
    udpClient.tcpclient()
