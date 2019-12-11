from PyQt5 import QtCore, QtGui, QtWidgets
from registerWindow import registerWindow
from friWindow import friWindow
from loginWindowFuncs import loginFuncs
from windowUi import *
from util import *

class loginWindow(publicWindow):
    textCtrl=""     #label to show info
    lf=loginFuncs() #alias for namespace store login functions
    loginBut=""     
    accIn=""
    pwIn=""
    _uiClass=Ui_loginWindow

    def __init__(self,loginBut,registerBut,accountInput,passwordInput,showLab):
        print(self._Dialog)
        super(loginWindow,self).__init__()
        #self.__Dialog=initWin(Ui_loginWindow)
        #alias
        dialog=self._Dialog
        #bind button onclick event
        dialog.findChild(QtWidgets.QPushButton,loginBut).clicked.connect(self.login)
        dialog.findChild(QtWidgets.QPushButton,registerBut).clicked.connect(self.register)
        #set handle
        self.textCtrl=self._Dialog.findChild(QtWidgets.QLabel,showLab)
        self.accIn=self._Dialog.findChild(QtWidgets.QLineEdit,accountInput)
        self.pwIn=self._Dialog.findChild(QtWidgets.QLineEdit,passwordInput)
    
    def login(self):
        'function after click login button'
        print('onClickLogin')
        print('account:'+self.accIn.text())
        print('password:'+self.pwIn.text())
        #check if account and pw format valid
        if not (self.lf.isAccValid(self.accIn.text()) and self.lf.isPwValid(self.pwIn.text())):
            print('invalid acc or pw')
            self.showInfo(self.lf.wrongText)
            return
        print('valid acc and pw')
        jstr=jsonGene('login',{'acc':self.accIn.text(),'pw':self.pwIn.text()})
        #send jstr to server and wait for reply
        """
        do disable all controls and display waiting animate()
        wait for reply from server()
        """
        print('now xhr')
        jstr=XHR(jstr)
        #login ok,open friends window
        if jstr['status']=='true':
            """
            dont show login window now()
            open friends window()
            """
            self.friWin=friWindow()
            self.friWin.show()
            self._Dialog.hide()
        #login fail,show exception
        else:
            """
            show exception info()
            undisable all controls and hide wating animate()
            """
    
    def register(self):
        'function after click register button'
        print('onClickRegister')
        #window must be member varieble or will be destroyed 
        self.regWin=registerWindow()
        print('1')
        self.regWin.show()

    def showInfo(self,text):
        'show text at text control in login window'
        try:
            self.textCtrl.setText(text)
        except:
            print('textCtrl wrong')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    h=loginWindow(loginBut='loginBut',registerBut='registerBut',\
                    accountInput='accountInput',passwordInput='passwordInput',\
                    showLab='showLab')
    h.show()
    sys.exit(app.exec_())
