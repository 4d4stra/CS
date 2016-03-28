from binary_tree_node import *
#defining a binary search tree

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.description = "This is a binary search tree"
        self.author = "Shawn Roberts"

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    #search tree method
    #if inserting and key exists, replace
    def search(self,key,current_node,return_parent=False,find_match=False):
        if key==current_node.key:
            if find_match:
                return current_node
            elif return_parent:
                return current_node,0
        if key < current_node.key:
            if current_node.left!=None:
                if return_parent:
                    retnode,dirflag=self.search(key,current_node.left,return_parent=return_parent,find_match=find_match)
                    return retnode,dirflag
                if find_match:
                    match=self.search(key,current_node.left,return_parent=return_parent,find_match=find_match)
                    return match
            elif find_match:
                return None
            elif return_parent:
                return current_node,-1
        else:
            if current_node.right!=None:
                if return_parent:
                    retnode,dirflag=self.search(key,current_node.right,return_parent=return_parent,find_match=find_match)
                    return retnode,dirflag
                elif find_match:
                    match=self.search(key,current_node.right,return_parent=return_parent,find_match=find_match)
                    return match                  
            elif find_match:
                return None
            elif return_parent:
                return current_node,1
    
    #insertion
    def insert(self,key,data):
        if self.root!=None:
            retnode,dirflag=self.search(key,self.root,return_parent=True)
            if dirflag==0:
                retnode.data=data
            elif dirflag==-1:
                retnode.left=BTNode(key,data,parent=retnode)
            else:
                retnode.right=BTNode(key,data,parent=retnode)
        else:
            self.root = BTNode(key,data)
        self.size = self.size + 1

    #allows for bracket inserting; eg: myZipTree['Plymouth'] = 55446
    def __setitem__(self,key,data):
        self.insert(key,data)

    #get data for a given key
    def get(self,key,return_node=False):
        if self.root:
            res = self.search(key,self.root,find_match=True)
            if res!=None:
                if return_node==False:
                    return res.data
                else:
                    return res
            else:
                return None
        else:
            return None

    #override for bracket extraction; eg: myZipTree['Atkinson']
    def __getitem__(self,key):
        return self.get(key)

    #override the 'in' operator
    def __contains__(self,key):
        if self.get(key,self.root)!=None:
            return True
        else:
            return False

    #finding successor
    def get_successor(self,node):
        #leftmost of right tree
        tree2search=node.right
        if tree2search!=None:
            while tree2search.left!=None:
                tree2search=tree2search.left
        return tree2search

    #finding predecessor
    def get_predecessor(self,node):
        #leftmost of right tree
        tree2search=node.left
        if tree2search!=None:
            while tree2search.right!=None:
                tree2search=tree2search.right
        return tree2search

    #remove node; 3 cases, no children, 1 child, and 2 children
    def remove(self,node2remove):
        if node2remove.isLeaf():#no children
            if node2remove.isLeftChild():
                node2remove.parent.left=None
            else:
                node2remove.parent.right=None
            node2remove=None
        elif node2remove.HasBothChildren():#2 children
            #I think this works; parent should still point to same place?
            nodereplacement=self.get_predecessor(node2remove)
            if not nodereplacement.isLeaf():#has a child;must be right child,itself,child must be left child
                nodereplacement.parent.right=nodereplacement.left
                nodereplacement.left.parent=nodereplacement.parent         
            node2remove.key=nodereplacement.key
            node2remove.data=nodereplacement.data
            if nodereplacement.isLeftChild():
                nodereplacement.parent.left=None
            else:
                nodereplacement.parent.right=None
            nodereplacement=None
        else:#1 child
            if node2remove.isLeftChild():
                if node2remove.left!=None:
                    if not node2remove.isRoot():
                        node2remove.parent.left=node2remove.left
                    node2remove.left.parent=node2remove.parent
                else:
                    if not node2remove.isRoot():
                        node2remove.parent.left=node2remove.right
                    node2remove.right.parent=node2remove.parent
            else:
                if node2remove.left!=None:
                    if not node2remove.isRoot():
                        node2remove.parent.right=node2remove.left
                    node2remove.left.parent=node2remove.parent
                else:
                    if not node2remove.isRoot():
                        node2remove.parent.right=node2remove.right
                    node2remove.right.parent=node2remove.parent
            node2remove=None
        
        
    #delete method; wraps around remove
    def delete(self,key):
        if self.size > 1:
            node2remove=self.get(key,return_node=True)
            if node2remove!=None:
                self.remove(node2remove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')
  
    #overload the 'del' operator
    def __delitem__(self,key):
        self.delete(key)


mytree = BinaryTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"

print(mytree[6])
print(mytree[2])

print 6 in mytree
mytree.delete(2)
mytree.delete(3)
