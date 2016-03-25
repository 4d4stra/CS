import numpy as np
#defining a heap class
#useful for minimum computation
class Heap:
    def __init__(self):
        self.data=[]
        self.keys=[]
        self.nobjects = len(self.keys)
        self.description = "This is a heap structure; a container of objects and keys"
        self.author = "Shawn Roberts"

    #insertion
    def insert(self,key_i,data_i):
        #inserting
        self.keys.append(key_i)
        self.nobjects +=1
        self.data.append(data_i)
        #checking if parent is greater than;swapping if so
        newind=self.nobjects-1
        parind=(self.nobjects-1)/2
        while self.keys[newind]<self.keys[parind]:
            self.keys[newind],self.keys[parind]\
                =self.keys[parind],self.keys[newind]
            self.data[newind],self.data[parind]\
                =self.data[parind],self.data[newind]
            newind,parind=parind,parind/2
    
    #heapify; initialize heap in batch
    #def 
        
        
    #extract object with min key value
    def pop(self):
        #extracting return object
        self.nobjects-=1
        return_obj=self.data[0]
        #moving last position to the first
        self.keys[0]=self.keys[-1]
        self.data[0]=self.data[-1]
        self.keys=self.keys[:-1]
        self.data=self.data[:-1]
        #bubbling down
        parent_ind=1
        child1_ind=2
        child2_ind=3
        while (self.keys[child1_ind-1] or self.keys[child2_ind-1])\
              <self.keys[parent_ind-1]):
            if self.keys[child1_ind-1]<self.keys[child2_ind-1]:
                minchild=child1_ind
            else:
                minchild=child2_ind
            self.keys[parent_ind-1],self.keys[minchild-1]\
                =self.keys[minchild-1],self.keys[parent_ind-1]
            self.data[parent_ind-1],self.data[minchild-1]\
                =self.data[minchild-1],self.data[parent_ind-1]
            parent_ind=minchild
            child1_ind=minchild*2
            child2_ind=minchild*2+1
        return return_obj

    #extract object with min key value, without removing
    def peek(self):
        return self.data[0]

    #delete arbitrary key and bubble up
    #def delete(self,key):
