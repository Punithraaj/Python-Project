import sys
from collections import namedtuple
MIN_PID = 300
MAX_PID = 5000
TRUE = 1
FALSE =0

#Python Doesn't Contains Structure so we Can Use Class Instead of Structure
#Here I defined class called PIDTable Which Consists of 2 data Memebers/Variables
class PidTable:
    PID=0
    isAvailable=0

# Method for allocating the Process Availablity status and Process Id
def allocate_map(pidlist):
    print (sys.getsizeof(pid))
    if(pidlist is None):
        return -1
    pidlist[0].PID = MIN_PID;
    pidlist[0].isAvailable = TRUE;
    print(pidlist[0].PID)
    print(len(pidlist))
    for i in range(1,len(pidlist)):
        print (i)
        pidlist[i].PID=pidlist[i-1].PID+1
        pidlist[i].isAvailable = TRUE
    return 1;

# Method to get the currently allocated Process from a pool of available Process and change its Available status to false Since the current Process in been allocted for a process
def allocate_pid(pidlist):
    for i in range(0, len(pidlist)):
        if (pidlist[i].isAvailable == TRUE):
            pidlist[i].isAvailable=FALSE;
            print (pidlist[i].PID)
            return pidlist[i].PID;
    if (i == MAX_PID - MIN_PID + 1):
        return -1;

# Method to release the currently allocated Process and change its Available status to true
def release_pid(pid,pidlist):
    pidlist[pid-MIN_PID].isAvailable=TRUE;


num = MAX_PID - MIN_PID
pid = 0;
# PidList is a list of Class Object or we can call it as Array of Object
PidList = []
for i in range(num):
    PidList.insert(i,PidTable())
num=allocate_map(PidList)
if(num!=-1):
    pid=allocate_pid(PidList)
    if(pid!=-1):
        print("New Process Allocated Pid = ",pid);

    pid=allocate_pid(PidList)
    if(pid!=-1):
        print("New Process Allocated Pid = ",pid);

    pid=allocate_pid(PidList)
    if(pid!=-1):
        print("New Process Allocated Pid = ",pid);

    pid = allocate_pid(PidList)
    if (pid != -1):
        print("New Process Allocated Pid = ", pid);

    print("Process %d now Releasing = ", pid)
    release_pid(pid,PidList)

    pid=allocate_pid(PidList)
    if(pid!=-1):
        print("New Process Allocated Pid =",pid)