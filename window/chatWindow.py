from PyQt5 import QtCore, QtGui, QtWidgets
from windowUi import *
from customWidgets import *
from util import *
from datetime import datetime
import time

class chatListItem(customWidget):
    uiClass=Ui_chatListItem
    
    def __init__(self,data):
        super(chatListItem,self).__init__()
        self.findChild(QtWidgets.QLabel,'nick').setText(data['nick'])
        self.findChild(QtWidgets.QLabel,'date').setText(data['date'])
        self.findChild(QtWidgets.QTextBrowser,'text').setText(data['text'])


class chatListItemR(customWidget):
    'chatListItem aligned to right'
    uiClass=Ui_chatListItemR
    
    def __init__(self,data):
        super(chatListItemR,self).__init__()
        self.findChild(QtWidgets.QLabel,'nick').setText(data['nick'])
        self.findChild(QtWidgets.QLabel,'date').setText(data['date'])
        self.findChild(QtWidgets.QTextBrowser,'text').setText(data['text'])
        

class chatWindow(publicWindow):
    _uiClass=Ui_chatWindow
    
    def __init__(self,info,data):
        print('chatWindow init')
        super(chatWindow,self).__init__()
        print(info,data)
        #chatter personal info
        self.info=info
        #self.msg is handle for friWindow's message dict
        self.msg=data
        'Qt controls'
        self.msgList=self._Dialog.findChild(QtWidgets.QVBoxLayout,'messageList')
        self.tEdit=self._Dialog.findChild(QtWidgets.QTextEdit,'textarea')
        self.sendBut=self._Dialog.findChild(QtWidgets.QPushButton,'sendBut')
        #let scroll area automate scroll to bottom when new msg come
        self.scrollBar=self._Dialog.findChild(QtWidgets.QScrollArea,'scrollArea').verticalScrollBar()
        self.scrollBar.rangeChanged.connect(lambda:self.scrollBar.setValue(self.scrollBar.maximum()))
        self.sendBut.clicked.connect(self.sendMsg)
        print('sort message')
        #sort messages in time,store in msg
        msg=[]
        for m in self.msg['send']:
            tmp=m
            tmp['send']=1
            msg.append(tmp)
        for m in self.msg['recv']:
            tmp=m
            tmp['send']=0
            msg.append(tmp)
        #sort with time as key
        msg=sorted(msg,key=lambda m:int(m['time']))
        print('push messageBox')
        for m in msg:
            self.pushMessageBox(m['send'],str(datetime.fromtimestamp(int(m['time']))),m['data'])
        self.sortedMsg=msg
            
    def pushMessageBox(self,send,date,text):
        'push message box into message list scroll'
        msgClass=''
        nick=''
        if send==1:
            msgClass=chatListItemR
            nick=self.info['from']['nick']
        else:
            msgClass=chatListItem
            nick=self.info['to']['nick']
        print(msgClass)
        msg=msgClass({'nick':nick,
                        'date':date,
                        'text':text})
        msg.setFixedHeight(80)
        self.msgList.addWidget(msg)

    def maintainMsg(self,send,text,time):
        'insert new msg into data structures'
        self.sortedMsg.append({'data':text,'time':time,'send':send})
        self.msg['send' if send==1 else 'recv'].append({'data':text,'time':time})
            
    def recvMsg(self,data):
        'recv new chatter message from server,called by friWindow'
        self.maintainMsg(send=0,text=data.data,time=data.time)
        self.pushMessageBox(send=0,date=str(datetime.fromtimestamp(data.time)),text=data.data)
        
    def sendMsg(self):
        'user click sendmsg button'
        print('send msg')
        txt=self.tEdit.toPlainText()
        nowTime=datetime.now().timestamp()
        try:
            XHR({'ope':'3',
                          'from':self.info['from']['id'],
                          'to':self.info['from']['id'],
                          'data':txt,
                          'time':nowTime})
        except:
            log('send msg to server failed!')
            return
        self.maintainMsg(send=1,time=str(nowTime),text=txt)
        self.pushMessageBox(send=1,date=str(datetime.fromtimestamp(nowTime)),text=txt)
        self.tEdit.setText('')
        
    def show(self):
        super(chatWindow,self).show()

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fri = chatWindow(info={
            'from':{'nick':'lpj','id':'19170306'},
            'to':{'nick':'wjy','id':'????????'}
            },data={'send':[{'data':'1th data','time':'1000000'},{'data':'2th data','time':'2000000'},
                      {'data':'3th data','time':'3000000'},{'data':'4th data','time':'4000000'}],
              'recv':[{'data':'1th data','time':'1002000'},{'data':'2th data','time':'2002000'},
                      {'data':'3th data','time':'3002000'},{'data':'4th data','time':'4002000'}],
            }
            )
    fri.show()
    sys.exit(app.exec_())

