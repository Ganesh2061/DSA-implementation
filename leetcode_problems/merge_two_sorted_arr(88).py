#we have two sorted array first array have certain m element, and second have n element, also first array have equal space to kept n element as well n+m element

def merge(num1, m, num2, n):
        num1_last_idx=m+n-1
        i=m-1
        j=n-1
        while(i>=0 and j>=0):
            if num1[i]>=num2[j]:
                num1[num1_last_idx]=num1[i]
                i=i-1
            else:
                num1[num1_last_idx]=num2[j]
                j=j-1
            num1_last_idx -=1
        while j>=0:
            num1[num1_last_idx]=num2[j]
            num1_last_idx -= 1
            j -=1
        
        for i in num1:
            print(i)
    
num1=[1,2,3,0,0,0]
num2=[2,5,6]
m=3
n=3
merge(num1,m,num2,n)