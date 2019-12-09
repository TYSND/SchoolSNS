import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
 
import socket
 
class UdpServer(object):
    def tcpServer(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('', 9527))       # 绑定同一个域名下的所有机器
        sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock2.bind(('', 9528))       # 绑定同一个域名下的所有机器  
        revcData, (remoteHost, remotePort) = sock.recvfrom(1024)
        print("[%s:%s] connect" % (remoteHost, remotePort))     # 接收客户端的ip, port

        sendDataLen = sock.sendto("this is send  data from server".encode(), (remoteHost, remotePort))
        print("revcData: ", revcData)
        print("sendDataLen: ", sendDataLen)		
        while True:
            revcData, (remoteHost, remotePort) = sock2.recvfrom(1024)
            print("[%s:%s] connect" % (remoteHost, remotePort))     # 接收客户端的ip, port
            
            sendDataLen = sock.sendto("this is send  data from server".encode(), (remoteHost, remotePort))
            print("revcData: ", revcData)
            print("sendDataLen: ", sendDataLen)
            
        sock.close()
        sock2.close()
            
if __name__ == "__main__":
    udpServer = UdpServer()
    udpServer.tcpServer()
