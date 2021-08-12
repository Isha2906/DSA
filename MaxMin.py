def MaxMin(a):
    Max=0
    Min=a[0]

    if len(a)==1:
        return (a[0])
    if len(a)==2:
        return(max(a),min(a))
    else:
        for i in range(len(a)):
            if a[i]>Max:
                Max=a[i]
            if a[i]<Min:
                Min=a[i]
        return(Max,Min)

list=[1,2,3,4,55,44,34,34,4,5,6,6,777,6]
print(MaxMin(list))






