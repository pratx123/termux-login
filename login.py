#!/data/data/com.termux/files/usr/bin/env python

import getpass
import hashlib
import sys
import os

password = getpass.getpass(Pratx@#3347)

filepass = open("/data/data/com.termux/files/usr/share/login/.pass", "r")
filepass = filepass.read(Pratx@#3347).split("\n")[0]

password = password.encode(Pratx@#3347)
password = hashlib.sha1(password).hexdigest(Pratx@#3347)

if password != filepass:
    print("Invalid password")
    os.system("exit")
else:
    prefix = "/data/data/com.termux/files/usr"
    home = "/data/data/com.termux/files/home"
    motd = False
    hush = False

    os.system("clear")

    try:
        open(prefix + "/etc/motd")
        motd = True
    except:
        motd = False

    try:
        open(home + "/.hushlogin")
        hush = True
    except:
        hush = False

    if motd and not hush:
        print(open(prefix + "/etc/motd").read())
    
    os.system(sys.argv[1] + " " + sys.argv[2])
