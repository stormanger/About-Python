import os
import time

source = ['/Users/zichun.wan/work/books']
target_dir = '/Users/zichun.wan/work/bookbackup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

#target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
#target = today + os.sep + now + '.zip'

comment = input('Enter a comment --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + comment.replace(' ', '_') + '.zip'

if not  os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

zip_cmd = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('Zip command is:')
print(zip_cmd)
print('Running:')
if os.system(zip_cmd) == 0:
    print('Successful backup to', target)
else:
    print('Backup failed')