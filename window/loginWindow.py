from PyQt5 import QtCore, QtGui, QtWidgets
from registerWindow import registerWindow
from friWindow import FriWindow
from loginWindowFuncs import loginFuncs
from windowUi import *
from util import *
import udpClient

class loginWindow(publicWindow):
    showInfo=""     #label to show info
    lf="" #alias for namespace store login functions
    loginBut=""
    accIn=""
    pwIn=""
    _uiClass=Ui_loginWindow

    def __init__(self,loginBut,registerBut,accountInput,passwordInput,showInfo):
        # receive thread start
        global receiver
        super(loginWindow,self).__init__()
        dialog=self._Dialog
        self.lf=loginFuncs(self._Dialog)
        #set handle
        self.showInfo=dialog.findChild(QtWidgets.QLabel,showInfo)
        self.accIn=dialog.findChild(QtWidgets.QLineEdit,accountInput)
        self.pwIn=dialog.findChild(QtWidgets.QLineEdit,passwordInput)
        self.loginBut=dialog.findChild(QtWidgets.QPushButton,loginBut)
        self.registerBut=dialog.findChild(QtWidgets.QPushButton,registerBut)
        #bind button onclick event
        self.loginBut.clicked.connect(self.login)
        self.registerBut.clicked.connect(self.register)
        
        
    def login(self):
        'function after click login button'
        log('onClickLogin','account:',self.accIn.text(),'password:',self.pwIn.text())
        #check if account and pw format valid
        if not (self.lf.isAccValid(self.accIn.text()) and self.lf.isPwValid(self.pwIn.text())):
            log('invalid acc or pw')
            self.showInfo(self.lf.wrongText)
            return
        log('valid acc and pw')
        jstr={'ope':opeDict('login'),'id':self.accIn.text(),'pw':self.pwIn.text()}
        log(self.lf.ctrlDict)
        #disable window,send jstr to server and wait for reply
##        self.lf.disableWindow()
##        log('disable ok')
        jstr=XHR(jstr)

    def loginCallback(self,jstr):
        """callback func after receive"""
        log('xhr ok')
##        self.lf.enableWindow()
##        log('enable ok')
        #login ok,open friends window
        if jstr['status']=='1':
            log('login success')
            try:
                #need data param for friWindow
                self.friWin=FriWindow(jstr)
                self.friWin.show()
                self._Dialog.hide()
            except:
                log('show window fail')
        #login fail,show
        elif jstr['status']=='0':
            log('login fail')
            self.showInfo.setText(jstr['info'])
            """
            show exception info()
            undisable all controls and hide wating animate()
            """
        else:
            self.showInfo.setText('服务器回复异常')
            log('unknown server reply')
    
    def register(self):
        'function after click register button'
        print('onClickRegister')
        #window must be member varieble or will be destroyed 
        self.regWin=registerWindow()
        self.regWin.show()

    def showInfo(self,text):
        'show text at text control in login window'
        try:
            self.textCtrl.setText(text)
        except:
            print('textCtrl wrong')


if __name__ == "__main__":
    import sys
    jstrDic={
        "ope":0
    }
    import json
    jstr=json.dumps(jstrDic)
    #must send first msg to server
    #to make receiver valid
    udpClient.cliSock.send(jstr)
    udpClient.receiver.start()
    #udpClient.init()
    app = QtWidgets.QApplication(sys.argv)
    h=loginWindow(loginBut='loginBut',registerBut='registerBut',\
                    accountInput='accountInput',passwordInput='passwordInput',\
                    showInfo='showLab')
    h.show()
    sys.exit(app.exec_())