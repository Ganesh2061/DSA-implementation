class stackimplementation:
  
  def __init__(self,size):
     self.size=size
     self.stack=[None]* size
     self.top=-1

  def push(self,item):
    if self.top < self.size-1:
         self.top += 1
         self.stack[self.top]=item
         
         
    else:
       print("stack is full")
     
  def pop(self):
    if self.top == -1:
       print("stack is empty")
    else:
       popped_item= self.stack[self.top]
       self.stack[self.top]=None
       self.top -= 1
       print("Removed item is",popped_item)
  def peek(self):
    if self.top == -1:
       print("stack is empty")
    else:
      peak_item=self.stack[self.top]
      print("peek item is ",peak_item)

  def display(self):
    if self.top==-1:
       print("Stack is empty")
    print("Stack element are")
    while self.top!=-1:
       print(self.stack[self.top]) 
       self.top -= 1



stackobject = stackimplementation(4)
stackobject.push(2)
stackobject.push(4)
stackobject.push(6)
stackobject.pop()
# stackobject.push(7)
# stackobject.push(29)
stackobject.display()