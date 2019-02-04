import threading
import time
import random
MIN_PID = 300
MAX_PID = 5000
NUM_THREADS = 100
YES = 0
NO =1
sem = threading.Semaphore()
#Python Doesn't Contains Structure so we Can Use Class Instead of Structure
#Here I defined class called PIDTable Which Consists of 2 data Memebers/Variables
class PidTable:
    PID=0
    isAvailable=0

# Method for allocating the Process Availablity status and ProcessId
def allocate_map(pidlist):
    if(pidlist is None):
        return -1
    pidlist[0].PID = MIN_PID;
    pidlist[0].isAvailable = YES;
    print(pidlist[0].PID)
    print(len(pidlist))
    for i in range(1,len(pidlist)):
        pidlist[i].PID=pidlist[i-1].PID+1
        pidlist[i].isAvailable = YES
    return 1;

# Method to get the currently allocated Process from a pool of available Process and change its Available status to false Since the current Process in been allocted for a process
def allocate_pid(pidlist):
    for i in range(0, len(pidlist)):
        if (pidlist[i].isAvailable == YES):
            pidlist[i].isAvailable=NO;
            print (pidlist[i].PID)
            return pidlist[i].PID;
    if (i == MAX_PID - MIN_PID + 1):
        return -1;

# Method to release the currently allocated Process and change its Available status to true
def release_pid(pid,pidlist):
    pidlist[pid-MIN_PID].isAvailable=YES;


def processStart(PidList):
    #A semaphore manages an internal counter which is decremented by each acquire() call and incremented by each release() call.
    # The counter can never go below zero; when acquire() finds that it is zero, it blocks, waiting until some other thread calls release().

    #Acquire a semaphore.decrement it by one and return immediately.

    # If it is zero on entry, block, waiting until some other thread has called release() to make it larger than zero.
    #Once the semaphore is being acquired by a particular thread then it should be released by that thread so that other thread can used the function
    sem.acquire()

    pid = allocate_pid(PidList)
    time.sleep(10000 / 1000000.0)
    if (pid != -1):
        print("Thread "+ str(threading.currentThread())+ " runnning....\n")
        print("New Process Allocated Pid = "+ str(pid)+"\n")
        executionTime = random.random() % 10
        time.sleep(executionTime)
        print("Process "+str(pid)+ " releasing pid \n");
        release_pid(pid,PidList);

    #Release a semaphore, incrementing the internal counter by one. When it was zero on entry and another thread is waiting for it to become larger than zero again, wake up that thread.
    sem.release()


num = MAX_PID - MIN_PID
pid = 0;
# PidList is a list of Class Object or we can call it as Array of Object
PidList = []
for i in range(num):
    PidList.insert(i,PidTable())
num=allocate_map(PidList)
ret =0
threads = []

#Here i am creating a list of threads for the given range each thread will be accessing same function
#processStart and i am passing the arguments to it.
for i in range(NUM_THREADS):
    threads.append(threading.Thread(target=processStart,args=[PidList]))
    threads[-1].start()

 #ait until the thread terminates.
# This methods will blocks the calling thread until the thread whose join() method is called terminates,
# either normally or through an unhandled exception – or until the optional timeout occurs.
for t in threads:
        t.join()

# if(num!=-1):
#     pid=allocate_pid(PidList)
#     if(pid!=-1):
#         print("New Process Allocated Pid = ",pid);
#
#     pid=allocate_pid(PidList)
#     if(pid!=-1):
#         print("New Process Allocated Pid = ",pid);
#
#     pid=allocate_pid(PidList)
#     if(pid!=-1):
#         print("New Process Allocated Pid = ",pid);
#
#     pid = allocate_pid(PidList)
#     if (pid != -1):
#         print("New Process Allocated Pid = ", pid);
#
#     print("Process %d now Releasing = ", pid)
#     release_pid(pid,PidList)
#
#     pid=allocate_pid(PidList)
#     if(pid!=-1):
#         print("New Process Allocated Pid =",pid)

