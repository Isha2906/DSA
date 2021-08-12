list=[1,2,3,4,5]
print(list)
start=0
n=len(list)
end=n-1
while(start<end):
    list[start],list[end]=list[end],list[start]
    start+=1
    end-=1
end

print(list)
