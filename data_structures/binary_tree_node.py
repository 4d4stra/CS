class BTNode:
    def __init__(self,key,data,left=None,right=None,parent=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def LeftChild(self):
        return self.left

    def RightChild(self):
        return self.right

    def Parent(self):
        return self.parent

    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChild(self):
        return self.parent and self.parent.right == self

    def isRoot(self):
        return self.parent==None

    def HasBothChildren(self):
        return self.right!=None and self.left!=None
    
    def isLeaf(self):
        return self.right==None and self.left==None
