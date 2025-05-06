def selection_sort():
    list=[2,4,3,7,6,23,17]
    n=len(list)

    for i in range(n-1):
        minindex=i
        
        for j in range(i+1,n):
            if list[j]<list[minindex]:
                minindex=j
            
        temp=list[i]
        list[i]=list[minindex]
        list[minindex]=temp

    for i in list:
        print(i)


selection_sort()