#First: $ pip3 install pexpect 
#The log.txt will be create after run program under this file path
#How to use it: $ python3 uploadFileToXXserver-v2.py
#Than input soure file path

import pexpect
import getpass
import datetime
import os

target_path = '/home'
target_server = '192.168.0.1'
target_user = 'ubuntu'
source = input('Please input source path:')
passwd = getpass.getpass('passwd: ')

cmd = "/usr/bin/rsync -avP {0} {1}@{2}:{3}".format(source, target_user, target_server, target_path)
cmd_byte = bytes(cmd, 'utf-8')
time = bytes(str(datetime.datetime.now()), 'utf-8')
fout = open('log.txt', 'wb')
fout.write(b"========================" + time + b"===========================\r\n")

if not os.path.exists(source):
    print('Source PATH is not exist, please check your input')
else:
    try:
        p = pexpect.spawn(cmd)
        fout.write(b'Commond is: ' + cmd_byte + b'\r\n')
        p.logfile_read = fout
        #print(p.logfile)
        p.expect('password: ')
        p.sendline(passwd)
        p.read()
        p.close()
        print('commond is:')
        print(cmd)
        print('Commond running:')
        print(str(p.before, 'utf-8'))
    except:
        print('Error')
