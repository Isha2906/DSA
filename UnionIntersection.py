l1=[1,2,3,5]
l2=[3,4,5,7]
l3=[5,6,7,8]
l4=[1,3,5,7]

def Union(l1,l2,l3,l4):
    l = []
    for i in l1:
        if i not in l:
            l.append(i)
    for i in l2:
        if i not in l:
            l.append(i)
    for i in l3:
        if i not in l:
            l.append(i)
    for i in l4:
        if i not in l:
            l.append(i)
    print(l)

Union(l1,l2,l3,l4)

def Intersection(l1,l2,l3,l4):
    l=[]
    for i in l1:
        if i in l2:
            if i in l3:
                if i in l4:
                    l.append(i)
                else:
                    print('No iintersection')
    print(l)

Intersection(l1,l2,l3,l4)