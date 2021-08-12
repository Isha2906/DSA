def SmallestKth(a,k):
   a.sort(reverse=True)
   return(a[k-1])

list=[1,2,333,444,5,345,77,5,6,4,8,88,90,67]
print(SmallestKth(list,2))
