import time
import shutil
import os

path= "C:/Users/12029/Documents/WhiteHatProjects/class"
time=time.time()

os.path.exists(path)
os.walk(path)
os.path.join(path)
cTime=os.stat(path).st_ctime
if(time>cTime):
    os.remove(path)
else:
        shutil.rmtree()

if(path.exists(path)=="false"):
    print("This file doesn't exist")