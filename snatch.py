import os
import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
XIP = str(s.getsockname()[0])
s.close()

from datetime import date
today = date.today()
DOE = str(today)

from datetime import datetime
now = datetime.now()
TOE = now.strftime("%H:%M:%S")

xfile = open('iplog.php','a')
xfile.write(XIP+' visited on '+DOE+' @ '+TOE)
xfile.write("\n")
xfile.close()
