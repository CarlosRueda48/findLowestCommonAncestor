class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def getPathToNode(root, target, path):
    if(root is None):
        return False

    if(root == target):
        return True

    path.append(root)

    #Check if target is in left subtree
    if(root.left):
        if(getPathToNode(root.left, target, path)):
            return True
    #Check if target is in right subtree
    if(root.right):
        if(getPathToNode(root.right, target, path)):
            return True

    path.pop()
    return False

def findCommonAncestor(root, n1, n2):
    path1 = []
    path2 = []
    print("Finding path to n1")
    getPathToNode(root, n1, path1)
    print("Finding path to n2")
    getPathToNode(root, n2, path2)
    print("Path to n1")
    for n in path1:
        print(n.val)
    print("Path to n2")
    for n in path2:
        print(n.val)
    i = 0
    while(i < len(path1) and i < len(path2)): 
        if path1[i] != path2[i]: 
            break
        i += 1
    return path1[i-1] 


root = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
six = TreeNode(6)
seven = TreeNode(7)

root.left = two
root.right = three
two.left = four
two.right = five
five.left = six
six.left = seven

#  
#        1
#      /   \  
#    2      3
#   /   \     
#  4     5
#      /  
#    6 
#   /
#  7  
  
n = findCommonAncestor(root, four, seven) # Expecting 2 
print("Common ancestor:")
print(n.val)