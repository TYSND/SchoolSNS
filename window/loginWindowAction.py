from PyQt5 import QtCore, QtGui, QtWidgets
from registerWindow import Ui_registerWindow

##this class handles all signals in login window

class loginWindowHandler:
    'handler for dialog,accout line input,password line input'
    Dialog=""
    loginBut=""
    accIn=""
    pwIn=""

    def __init__(self,dialog,loginBut,registerBut,accountInput,passwordInput):
        self.Dialog=dialog
        #bind onclick func to loginBut
        dialog.findChild(QtWidgets.QPushButton,loginBut).clicked.connect(self.login)
        #bind onclick func to registerBut
        dialog.findChild(QtWidgets.QPushButton,registerBut).clicked.connect(self.register)
        #set handle
        self.accIn=self.Dialog.findChild(QtWidgets.QLineEdit,accountInput)
        self.pwIn=self.Dialog.findChild(QtWidgets.QLineEdit,passwordInput)

    
    def login(self):
        'function after click login button'
        print('onClickLogin')
        print('account:'+self.accIn.text())
        print('password:'+self.pwIn.text())
        #check if account and pw format valid
        """
        if (!is login Info Ok())
            do Exception()
        """
        jstr=jsonGene('login',{'acc':self.accIn.text(),'pw':self.pwIn.text()})
        #send jstr to server and wait for reply
        """
        do disable all controls and display waiting animate()
        wait for reply from server()
        jstr=serverReply()
        """
        #login ok,open friends window
        if jstr.status=='true':
            """
            dont show login window now()
            open friends window()
            """
        #login fail,show exception
        else:
            """
            show exception info()
            undisable all controls and hide wating animate()
            """


    def register(self):
        'function after click register button'
        print('onClickRegister')
        regWin=QtWidgets.QDialog()
        #program crashes if set regWin as an attribute
#        self.regWin=QtWidgets.QDialog()
        ui = Ui_registerWindow()
        ui.setupUi(regWin)
        regWin.exec_()
        #regWin.show()
#        self.regWin.show()

    def jsonGene(action,dataDict):
##        standard method to generate json to send.simply add
##            'action' key to dataDict.
        dataDict.action=action
        return dataDict
