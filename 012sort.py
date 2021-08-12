list=[1,1,1,2,2,2,2,2,1,1,1,0,0,0,1,0,2,0,2,0,1,1,2,0,1]

lower = 0
mid = 0
high = len(list) - 1

while (mid<=high):

    if list[mid]==0:
        list[lower],list[mid]=list[mid],list[lower]
        lower=lower+1
        mid=mid+1

    elif list[mid]==1:
        mid=mid+1

    elif list[mid]==2:
        list[mid],list[high]=list[high],list[mid]
        high=high-1
    else:
        print('Array contains an invalid input')

print(list)






