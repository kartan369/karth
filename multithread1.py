import threading
import time
import _thread

def printtime(threadname, threaddelay):
    count = 0
    while count < 3:
        time.sleep(threaddelay)
        count = count+1
        print("%s %s"%(threadname,time.ctime(time.time())))

#example to creat two threads

try:
    _thread.start_new_thread(printtime, ("first thread",3,  )   )
    _thread.start_new_thread(printtime, ("second thread",9, )   )
except:
    print("Unable to start thread")

while 1:
    pass
