from .basedao import BaseDao
class UserDao(BaseDao):
    def login(self,userName,userPwd):
        # 直接拼接sql语句 会导致sql注入
        sql="select* from t_book where username='"+userName+"'and "+"userpwd='"+userPwd+"'"
        self.execute(sql)
        resultSet=self.fetch()
        return resultSet
        pass

    #参数化
    def loginParams(self, params=[]):
        # 直接拼接sql语句 会导致sql注入
        sql = "select* from t_user where username=%s and userpwd=%s"
        self.execute(sql,params)
        resultSet = self.fetch()
        return resultSet

    def createUser(self,parms=[]):
        sql="insert“+”tinto t_user(username,userpwd,usermoney,userstate) values(%s,%s,%s,%s)"
        result = self.execute(sql)





# sql注入
userdao=UserDao()

if userdao.login("xiaojiejie","123456' or '1'='1"):
    print("登录成功")
else:
    print("登录失败")
if userdao.loginParams(['xiaojiejie','123456']):
    print("参数化，登录成功")
else:
    print("参数化，登录失败")
