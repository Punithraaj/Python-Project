#Array leftRotation and right rotation

Arr=[1,2,3,4,5] #array/List
d=7 #No of Rotation

def leftrotate(arr,d):
    n = len(arr) #len of Array/list
    if(d>n):
        d=d%n
    Arr1=[]
    print (d)
    for i in range(n):
        new = (i+(n-d))%n
        print (new)
        Arr1.insert(new,arr[i])
    print (Arr1)
def rightrotate(arr, d):
    n = len(arr)
    if (d > n):
        d = d % n
    Arr1 = []
    for i in range(n):
        new = (((i -d))+n % n)
        Arr1.insert(i, arr[new])
    print(Arr1)
leftrotate(Arr,d)
rightrotate(Arr,d)