from PyQt5 import QtCore, QtGui, QtWidgets
from windowUi import *
from customWidgets import *
from util import *
from chatWindow import *


class FriListItem(customWidget):
    """list item show friend info in friend window"""
    uiClass = Ui_friListItem
    friId = ""
    #   handle for friendWindow instance
    friW = ""

    def __init__(self, data, friW):
        super(FriListItem, self).__init__()
        self.friId = data['id']
        #       self.findChild(QtWidgets.QGraphicsView,'avatar').setAvatar
        self.findChild(QtWidgets.QLabel, 'nick').setText(data['nick'])
        self.findChild(QtWidgets.QLabel, 'account').setText(data['id'])
        self.findChild(QtWidgets.QLabel, 'status').setText('在线' if data['online'] == '1' else '离线')
        self.findChild(QtWidgets.QPushButton, 'message').setText(
            ((str(data['unread']) + '条') if data['unread'] > 0 else '没有') + '新消息')
        self.setFixedHeight(85)
        self.friW = friW
        self.findChild(QtWidgets.QPushButton, 'message').clicked.connect(self.openChatWin)

    def openChatWin(self):
        id = self.friId
        'open chat window and unread message'
        print(
            {'from': {'nick': self.friW.you['nick'], 'id': self.friW.you['id']},
             'to': {'nick': self.friW.fri[id]['nick'], 'id': id}
             })
        print(self.friW.message[id])
        try:
            self.friW.chatWindows[id] = chatWindow(info={
                'from': {'nick': self.friW.you['nick'], 'id': self.friW.you['id']},
                'to': {'nick': self.friW.fri[id]['nick'], 'id': id}
            },
                data=self.friW.message[id])
            self.friW.chatWindows[id].show()
        except:
            print('chat window show fail')


class FriWindow(publicWindow):
    _uiClass = Ui_friWindow
    # handle for all Qt controls
    ctrl = {}
    # your friends
    fri = {}
    # store qt window handle
    chatWindows = {}
    # acquaintance not friends but invited
    acqt = {}
    message = {}

    def __init__(self, data):
        super(FriWindow, self).__init__()
        self.you = data['you']
        # store message with id as index
        for chatter in data['message']:
            self.message[chatter['id']] = {
                'send': chatter['send'],
                'recv': chatter['receive']
            }

        for invitation in data['invite']:
            if invitation['status'] == '1':
                self.fri[invitation['id']] = invitation
            else:
                self.acqt[invitation['id']] = invitation

                # set handle
        self.ctrl['nick'] = self._Dialog.findChild(QtWidgets.QLabel, 'nick')
        self.ctrl['avatar'] = self._Dialog.findChild(QtWidgets.QGraphicsView, 'avatar')
        self.ctrl['id'] = self._Dialog.findChild(QtWidgets.QLabel, 'account')
        self.ctrl['friList'] = self._Dialog.findChild(QtWidgets.QVBoxLayout, 'friList')
        # connect event func
        self._Dialog.findChild(QtWidgets.QPushButton, 'friendInvite').clicked = self.clickFriInvite()
        self._Dialog.findChild(QtWidgets.QPushButton, 'addFriend').clicked = self.clickAddFriend()
        self._Dialog.findChild(QtWidgets.QPushButton, 'setting').clicked = self.clickSetting()
        # set your info
        self.ctrl['nick'].setText(self.you['nick'])
        self.ctrl['id'].setText(self.you['id'])
#       self.ctrl.avatar.setAvatar(self.you.avatar)
        # add friListItem into friList layout
        for id, friend in self.fri.items():
            unreadCnt = 0
            for msg in self.message[id]['recv']:
                if int(msg['readed']) == 0:
                    unreadCnt += 1
            newItem = FriListItem({
                'nick': friend['nick'],
                'avatar': friend['avatar'],
                'id': friend['id'],
                'unread': unreadCnt,
                'online': friend['online']
            }, self)
            # click nick or account to open chat window
            ##            newItem.findChild(QtWidgets.QLabel,'account').linkActivated.connect(self.openChatWin)
            ##            newItem.findChild(QtWidgets.QLabel,'nick').linkActivated.connect(
            ##                lambda:self.openChatWin(friend['id']))
            self.ctrl['friList'].addWidget(newItem)

    def openChatWin(self, id):
        """open  chat window and unread message"""
        print(
            {'from': {'nick': self.you['nick'], 'id': self.you['id']},
             'to': {'nick': self.fri[id]['nick'], 'id': id}
             })
        print(self.message[id])
        try:
            self.chatWindows[id] = chatWindow(info={
                'from': {'nick': self.you['nick'], 'id': self.you['id']},
                'to': {'nick': self.fri[id]['nick'], 'id': id}
            },
                data=self.message[id])
            self.chatWindows[id].show()
        except:
            print('chat window show fail')

    def clickFriInvite(self):
        pass

    def clickAddFriend(self):
        pass

    def clickSetting(self):
        pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    fri = FriWindow({
        'you': {
            'nick': 'lpj',
            'avatar': '2',
            'id': '19170306'
        },
        'invite': [
            {
                'from': '0',
                'id': '1',
                'nick': 'wjy',
                'avatar': '1',
                'status': '1',
                'online': '1',
            },
            {
                'from': '0',
                'id': '2',
                'nick': '2nd friend',
                'avatar': '2',
                'status': '1',
                'online': '1',
            },
            {
                'from': '0',
                'id': '3',
                'nick': '3rd friend',
                'avatar': '3',
                'status': '1',
                'online': '0',
            },
            {
                'from': '0',
                'id': '4',
                'nick': '4th friend',
                'avatar': '1',
                'status': '1',
                'online': '1',
            },
            {
                'from': '0',
                'id': '5',
                'nick': '5nd friend',
                'avatar': '2',
                'status': '1',
                'online': '1',
            },
            {
                'from': '0',
                'id': '6',
                'nick': '6th friend',
                'avatar': '3',
                'status': '1',
                'online': '0',
            },
        ],
        'message': [
            {
                'id': '1',
                'send': [{'data': '1th data', 'time': '1000000'}, {'data': '2th data', 'time': '2000000'},
                         {'data': '3th data', 'time': '3000000'}, {'data': '4th data', 'time': '4000000'}],
                'receive': [{'data': '1th data', 'time': '1002000', 'readed': '1'},
                            {'data': '2th data', 'time': '2002000', 'readed': '1'},
                            {'data': '3th data', 'time': '3002000', 'readed': '1'},
                            {'data': '4th data', 'time': '4002000', 'readed': '0'}],
            },
            {
                'id': '2',
                'send': [{'data': '1th data', 'time': '1000000'}, {'data': '2th data', 'time': '2000000'},
                         {'data': '3th data', 'time': '3000000'}, {'data': '4th data', 'time': '4000000'}],
                'receive': [{'data': '1th data', 'time': '1002000', 'readed': '1'},
                            {'data': '2th data', 'time': '2002000', 'readed': '1'},
                            {'data': '3th data', 'time': '3002000', 'readed': '1'},
                            {'data': '4th data', 'time': '4002000', 'readed': '1'}],
            },
            {
                'id': '3',
                'send': [{'data': '1th data', 'time': '1000000'}, {'data': '2th data', 'time': '2000000'},
                         {'data': '3th data', 'time': '3000000'}, {'data': '4th data', 'time': '4000000'}],
                'receive': [{'data': '1th data', 'time': '1002000', 'readed': '0'},
                            {'data': '2th data', 'time': '2002000', 'readed': '0'},
                            {'data': '3th data', 'time': '3002000', 'readed': '0'},
                            {'data': '4th data', 'time': '4002000', 'readed': '0'}],
            },
            {
                'id': '4',
                'send': [],
                'receive': [],
            },
            {
                'id': '5',
                'send': [],
                'receive': [],
            },
            {
                'id': '6',
                'send': [],
                'receive': [],
            }
        ]
    })
    fri.show()
    sys.exit(app.exec_())
