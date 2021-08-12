import numpy as np
my_array=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(my_array)

def RotateMatrix(array):
    n=len(array)
    for layer in range(n//2):
        first=layer
        last=n-layer-1
        for i in range(first,last):
            #save the top element
            top=array[layer][i]
            #move left to top
            array[layer][i]=array[-i-1][layer]
            #move bottom to left
            array[-i-1][layer]=array[-layer-1][-i-1]
            #move right to bottom
            array[-layer-1][-i-1]=array[i][-layer-1]
            #move to right
            array[i][-layer-1]= top
    return(array)
 
print(RotateMatrix(my_array))


