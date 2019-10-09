def inorder(root):  #中序遍历 “左中右”
    if root != None:
        inorder(root.left)
        print('[%2d]'%root.data, end = '')
        inorder(root.right)