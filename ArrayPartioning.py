
def arrayPartition(a):
    p_arr = []
    for i in a:
        if i==0:
            p_arr.append(i)
    for i in a:
        if i != 0:
            p_arr.append(i)
    return p_arr

print(arrayPartition([2,3,3,9,0,3,8,0]))