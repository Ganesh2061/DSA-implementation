def bubble_sort(): 
    list=[3,5,2,8,86,33,77]
    n=len(list)

    for i in range(n-1):
        j=0
        for j in range(n-i-1):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
            
    for i in list:
        print(i)

bubble_sort()

        
