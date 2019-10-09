def preorderTraversal(root): #前序遍历 “中左右” 递归
    if root != None:
        print('[%2d]'%root.data, end = '')
        preorderTraversal(root.left)
        preorderTraversal(root.right)