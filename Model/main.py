from Model.User import User
from Model.Filedata import Filedata
userObj=User(name,mail,phone,plan)
while True:
    choice=int(input())
    if choice==1:
        userObj.createFiles(value)
    elif choice==2:
        userObj.removeFiles()
    elif choice==3:
        userObj.viewFiles()
    elif choice==4:
        userObj.viewText()
    elif choice==5:
        userObj.modifyText(value)
    else:
        break


