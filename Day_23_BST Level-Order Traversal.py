def levelOrder(self,root):
        #Write your code here
        output = [root]
        for i in output:
            if i:
                print(i.data, end=" ")
                output.append(i.left)
                output.append(i.right)