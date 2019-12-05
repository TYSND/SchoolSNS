class loginFuncs:
    #store funcions used when login
    #exception info to show
    wrongText=""
    
    def isAccValid(self,account):
        'is account valid or not'
        if len(account)<=0:
            self.wrongText="账户不能为空"
            return False
        else:
            self.wrongText=""
            return True

    def isPwValid(self,pw):
        'is password valid or not'
        if len(pw)<=0:
            self.wrongText="密码不能为空"
            return False
        else:
            self.wrongText=""
            return True
