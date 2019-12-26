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
        #login ok,open friends window
        if str(jstr['status'])=='1':
            log('login success')
            try:
                #need data param for friWindow
                self.friWin=FriWindow(jstr)
                log('now show friWin')
                log(self.friWin)
                self.friWin.show()
                log('show friWin ok')
                self._Dialog.hide()
                log('hide dialog ok')
            except Exception as e:
                log('show window fail')
                log(e)
        #login fail,show
        elif str(jstr['status'])=='0':
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


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

if __name__ == "__main__":
    import sys
    import json

    # Back up the reference to the exceptionhook
    sys._excepthook = sys.excepthook

    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook
    #greet msg send first to server,
    #or receiver invalid
    jstrDic={"ope":0}
    jstr=json.dumps(jstrDic)
    udpClient.cliSock.send(jstr)
    udpClient.receiver.start()
    app = QtWidgets.QApplication(sys.argv)
    h=loginWindow(loginBut='loginBut',registerBut='registerBut',\
                    accountInput='accountInput',passwordInput='passwordInput',\
                    showInfo='showLab')
    udpClient.h=h
    h.show()
    try:
        sys.exit(app.exec_())
    except:
        print('exiting')
