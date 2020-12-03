import os
import pythonping as pig
import subprocess

a = os.system("ping 8.8.8.8",)
print(a)
print('OS прошла')

d = subprocess.call('ping 8.8.8.8')
print('sub прошёл')
b = pig.ping('8.8.8.8', count=1)
print('pig прошла')