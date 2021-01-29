def removeDuplicates(self,head):
        
        #Write your code here
        l = head
        while True:

            try:
                if l.data == l.next.data:
                    l.next =  l.next.next
                else:  
                    l  =  l.next
            except AttributeError: # final None has no data
                return head