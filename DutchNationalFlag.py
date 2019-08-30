#Dutch National Flag problem
def MoveToFront(a):
    boundary = 0
    for i in range(len(a)):
        if a[i]==0:
            #A[boundary],i = i, A[boundary]
            a[i], a[boundary] = a[boundary], a[i]
            boundary += 1
    return print(a)

MoveToFront([2,4,5,0,4,0,5])


def MoveToBack(a):
    boundary = len(a)-1
    for i in reversed(range(len(a))):
        if a[i]==0:
            a[i], a[boundary] = a[boundary], a[i]
            boundary-=1
    return print(a)

MoveToBack([2,4,5,0,4,0,5])


def DutchNationalFlag(a):
    pivot = 8
    i=0
    lb=0
    hb=len(a)-1
    while(i <= hb):
        if (a[i]<pivot):
            a[i], a[lb]=a[lb], a[i]
            lb+=1
            i+=1
        elif(a[i]>pivot):
            a[i], a[hb] = a[hb], a[i]
            hb-=1
        else:
            i+=1
    return print(a)

DutchNationalFlag([11,12,14,17,45,3,6,2,4,0,1,1,8,8,8])


