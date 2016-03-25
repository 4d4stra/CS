#defining a stack class
class Queue:
    def __init__(self):
        self.data=[]
        self.length = len(self.data)
        self.description = "This is a queue structure"
        self.author = "Shawn Roberts"

    #push and pop
    def pop(self):
        if self.length==0:
            return None
        else:
            self.length-=1
            return self.data.pop(0)

    def push(self,a):
        self.length+=1
        return self.data.append(a)
