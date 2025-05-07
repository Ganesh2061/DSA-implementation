def insertion_sort():
    list=[23,52,32,54,34,66]
    n=len(list)

    for i in range(n):
        curr=list[i]
        prev=i-1
        while prev>=0 and list[prev]>curr:
            list[prev+1]=list[prev]
            prev=prev-1

        list[prev+1]=curr
    

    for i in list:
        print(i)

insertion_sort()