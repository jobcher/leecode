#!/user/bin/python3
# 隐藏密码输入
import getpass
username = input("username:")
password = getpass.getpass()
if username == "jobcher" and password == "1234":
    print("login success")
else:
    print("login failed")