#defining a stack class
class Deque:
    def __init__(self):
        self.data=[]
        self.length = len(self.data)
        self.description = "This is a deque structure"
        self.author = "Shawn Roberts"

    #push and pop
    def left_pop(self):
        if self.length==0:
            return None
        else:
            self.length-=1
            return self.data.pop(0)

    def right_pop(self):
        if self.length==0:
            return None
        else:
            self.length-=1
            return self.data.pop()

    def right_push(self,a):
        self.length+=1
        return self.data.append(a)
    
    def left_push(self,a):
        self.length+=1
        return self.data.insert(0,a)
