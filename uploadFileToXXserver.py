#Please set pub-key first
#How to use it: $ python3 uploadFileToXXserver.py
#Than input soure file path

import os

target_path = '/home'
#target_path = '/tmp'
target_server = '192.168.0.1'
target_user = 'gpu1'

source = input('Please input source path:')

if not os.path.exists(source):
    print('Source PATH is not exist, please check your input')
else:
    rsync_cmd = '/usr/bin/rsync -avP {0} {1}@{2}:{3}'.format(source, target_user, target_server, target_path)
    print('Command is:')
    print(rsync_cmd)
    print('Command running:')
    if os.system(rsync_cmd) == 0:
        print('Successful upload files to 192.168.88.79/home/gpu1/data-digits/DataSets’)
    else:
        print('Upload failed')
