import threading
import time
import _thread


class myfirstthread(threading.Thread):
    def __init__(self,threadid,name,counter):
        threading.Thread.__init__(self)
        self.threadid = threadid
        self.name = name
        self.counter = counter
    def run(self):
        print("here the thread is starting",self.name)
        # now we are trying to get the lock to syncronize the thread
        threadLock.acquire()
        print_time(self.name,3,self.counter)
        # now we are releasing the lock for next thread
        threadLock.release()
        #print("Thread is exiting",self.name)
def print_time(tname,tcounter,tdelay):
    while tcounter:
        #if public_flag:
         #   tname.exit()
        time.sleep(tdelay)
        print("%s %s"%(tname,time.ctime(time.time())))
        tcounter = tcounter-1


threadLock = threading.Lock()
thread_data = []
# these are my new created threads
mft = myfirstthread(1,"thread1",1)
mft1 = myfirstthread(2,"thread2",2)
# here im going to start new thread
mft.start()
mft1.start()
# adding these threads to list(thread_data)
thread_data.append(mft)
thread_data.append(mft1)
# wait for all threads to complete
for item in thread_data:
    item.join()
    print("we are exiting from the main thread")
