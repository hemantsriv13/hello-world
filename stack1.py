class stack1:
    def __init__(self):
        self.stack=[] #creates a stack
    def isEmpty(self):
        if len(self)==0:
            return True
        return False        
    def push(self,ele):
        self.stack.append(ele)
    def peek(self):
        if(len(self.stack==0)):
            print("Empty stack")
            return -1
        return self.stack(len(self.stack)-1)
    def pop(self):
        if(len(self.stack)==0):
            print("Empty stack")
            return -1
        return self.stack.pop()
    def printStack(self):
        print(self.stack)
    
st1=stack1()
st1.push(5)
st1.push(4)
st1.pop()
print(st1)
st1.printStack()