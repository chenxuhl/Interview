def postorderTraversal(root): #后序遍历 "左右中" 递归
    if root != None:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print('[%2d]'%root.data, end = '')