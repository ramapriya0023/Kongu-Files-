from Model.Filedata import Filedata
class User:
    file=[]
    fileObj=Filedata()
    Filedata.filedata(plan)
    userPlan = input()
    if(userPlan=="freeplan"):
        userPlan = Filedata(0, 10, 15, 50, "No", "Yes")
    elif (userPlan=="pro plan"):
        userPlan = Filedata(1000, 100, None, 200, "Yes", "No")
    else:
        userPlan= Filedata(3000, 500, None, 1500, "Yes", "No")
    def __init__(self,name,mail,phone,plan):
        self.name=name
        self.mail=mail
        self.phone=phone
        self.plan=plan
    def createFiles(self,value):
        if len(User.file) > userPlan.storage_cap:
            print("Max storage attained")
        else:
            User.file=User.file.append(value)
    def removeFiles(self):
        User.file=[]
    def viewFiles(self):
        print(*User.file)
    def viewText(self):
        print("Name: {0}\n Mail: {1}\n Phone: {2}\n Plan: {3}".format(self.name,self.mail,self.phone,self.plan))
    def modifyText(self,value):
        edit=int(input("1.Name\n 2.Mail\n 3.Phone \n4.PLan"))
        if edit==1:
            self.name=value
        elif edit==2:
            self.mail=value
        elif edit==3:
            self.phone=value
        elif edit==4:
            self.plan=value

