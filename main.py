from InstagramOSINT import *
import twint
import snapchat
import sys

userName = input("Username: ")

try:
    instagram = InstagramOSINT(username=userName) 
    print("Found " + instagram['Username'] + " in Instagram")
except:
    print("Not found in Instagram")



me = snapchat.SnapChat(userName)
a = me.check_username()
if a == userName + ' is already taken!':
    print("Found " + userName + " on SnapChat")
else:
    print("Not found in Snapchat")


c = twint.Config()
c.Username = userName
twint.run.Lookup(c)