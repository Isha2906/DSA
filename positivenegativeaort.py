my_array=[1,-2,3,4,5,6-4,-6,-5,-77,-88,5,-6,-99,5,6,7,6,6]
mid=0
end=len(my_array)-1
while(mid<=end):
    if my_array[mid]>0  and  my_array[end]<0:
        my_array[mid],my_array[end]= my_array[end],my_array[mid]
        mid+=1
        end-=1
    elif my_array[mid]>0 and my_array[end]>0:
        end-=1
    elif my_array[mid]<0 and my_array[end]<0:
        mid+=1
    else:
        mid+=1
        end-=1

print(my_array)








