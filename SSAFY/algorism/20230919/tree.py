
# 연결리스트저장
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self,childNode):
        if not self.left:
            self.left = childNode
            return

        if not self.right:
            self.right = childNode
            return

        return

    def preorder(self):
        if self != None:
            print(self.value, end=' ')
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def inorder(self):
        if self != None:
            if self.left:
                self.left.inorder()
            print(self.value, end=' ')
            if self.right:
                self.right.inorder()

    def postorder(self):
        if self != None:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.value, end=' ')

arr = [1,2,1,3,2,4,3,5,3,6]
nodes = [TreeNode(i) for i in range(0,14)]

for i in range(0,len(arr),2):
    parentNode = arr[i]
    childNode = arr[i+1]
    nodes[parentNode].insert(nodes[childNode])

nodes[1].inorder()
