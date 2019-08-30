def DNF_Example(a):
    lb=0
    hb= len(a)-1
    i=0
    while(i<=hb):
        if(a[i]==0):
            a[i],a[lb] = a[lb], a[i]
            i+=1
            lb+=1
        elif(a[i]==2):
            a[i], a[hb] = a[hb], a[i]
            hb-=1
        else:
            i+=1
    #return a

    for i in range(len(a)):
        if a[i]==0:
            a[i]= 'Red'
        elif a[i]==1:
            a[i] = 'white'
        else:
            a[i]= 'Blue'
    return print(a)


DNF_Example([1,2,1,1,0])