from PyQt5 import QtCore, QtGui, QtWidgets
import udpClient
import json
serverIp=""
serverPort=0

def log(*string):
    print(*string)

def opeDict(opeName):
    'convert oepration name to operation code'
    dict={'login':'1','register':'2','send':'3','setting':'4',
          'search':'5','friendApply':'6','reviewApply':'7','offline':'8'}
    try:
        return dict[opeName]
    except:
        return 'wrong opeName'

def selectAvatar(avatarBef):
    return 8

class publicWindow:
    _Dialog=""
    def __init__(self):
        print('init')
        self._Dialog=initWin(self._uiClass)

    def show(self):
        self._Dialog.show()


def initWin(uiClass):
    'initial window and set ui,then return window'
    Dialog = QtWidgets.QDialog()
    try:
        ui = uiClass()
        ui.setupUi(Dialog)
    except:
        print('wrong ui class')
    return Dialog


def initWidget(uiClass):
    Widget = QtWidgets.QWidget()
    try:
        ui = uiClass()
        ui.setupUi(Widget)
    except:
        print('wrong ui class')
    return Widget


def jsonGene(action,dataDict):
##      standard method to generate json to send,simply add
##      'action' key to dataDict.
    dataDict['action']=action
    return dataDict

def XHR(payload):
    """
    like XmlHttpRequest,send one payload to server and
    wait for one reply then return
    """
    log('try XHR',json.dumps(payload))
    udpClient.cliSock.send(json.dumps(payload))
    log('send ok')
    return
    if True:
        return {
                'status':'1',
                'you':{
                    'nick':'lpj',
                    'avatar':'2',
                    'id':'19170306'
                },
                'invite':[
                    {
                        'from':'0',
                        'id':'1',
                        'nick':'wjy',
                        'avatar':'1',
                        'status':'1',
                        'online':'1',
                    },
                    {
                        'from':'0',
                        'id':'2',
                        'nick':'2nd friend',
                        'avatar':'2',
                        'status':'1',
                        'online':'1',
                    },
                    {
                        'from':'0',
                        'id':'3',
                        'nick':'3rd friend',
                        'avatar':'3',
                        'status':'1',
                        'online':'0',
                    },
                    {
                        'from':'0',
                        'id':'4',
                        'nick':'4th friend',
                        'avatar':'1',
                        'status':'1',
                        'online':'1',
                    },
                    {
                        'from':'0',
                        'id':'5',
                        'nick':'5nd friend',
                        'avatar':'2',
                        'status':'1',
                        'online':'1',
                    },
                    {
                        'from':'0',
                        'id':'6',
                        'nick':'6th friend',
                        'avatar':'3',
                        'status':'1',
                        'online':'0',
                    },
                ],
                'message':[
                    {
                        'id':'1',
                        'send':[{'data':'1th data','time':'1000000'},{'data':'2th data','time':'2000000'},
                                {'data':'3th data','time':'3000000'},{'data':'4th data','time':'4000000'}],
                        'receive':[{'data':'1th data','time':'1002000','readed':'1'},
                                   {'data':'2th data','time':'2002000','readed':'1'},
                                   {'data':'3th data','time':'3002000','readed':'1'},
                                   {'data':'4th data','time':'4002000','readed':'0'}],
                    },
                    {
                        'id':'2',
                        'send':[{'data':'1th data','time':'1000000'},{'data':'2th data','time':'2000000'},
                                {'data':'3th data','time':'3000000'},{'data':'4th data','time':'4000000'}],
                        'receive':[{'data':'1th data','time':'1002000','readed':'1'},
                                   {'data':'2th data','time':'2002000','readed':'1'},
                                   {'data':'3th data','time':'3002000','readed':'1'},
                                   {'data':'4th data','time':'4002000','readed':'1'}],
                    },
                    {
                        'id':'3',
                        'send':[{'data':'1th data','time':'1000000'},{'data':'2th data','time':'2000000'},
                                {'data':'3th data','time':'3000000'},{'data':'4th data','time':'4000000'}],
                        'receive':[{'data':'1th data','time':'1002000','readed':'0'},
                                   {'data':'2th data','time':'2002000','readed':'0'},
                                   {'data':'3th data','time':'3002000','readed':'0'},
                                   {'data':'4th data','time':'4002000','readed':'0'}],
                    },
                    {
                        'id':'4',
                        'send':[],
                        'receive':[],
                    },
                    {
                        'id':'5',
                        'send':[],
                        'receive':[],
                    },
                    {
                        'id':'6',
                        'send':[],
                        'receive':[],
                    }
                ]
            }
    else:
        return {'status':'0','info':'wrong password'}
    
