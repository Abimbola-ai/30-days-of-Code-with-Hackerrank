class Solution:
    # Write your code here
    def __init__(self): #initialize the variables
        self.stack = []
        self.queue = []
    
    def pushCharacter(self,char): #append char in stack
        self.stack.append(char)
    
    def enqueueCharacter(self,char): #append char in queue
        self.queue.append(char)
    
    def popCharacter(self):
        return(self.stack.pop(0)) # remove and return the first index 
    
    def dequeueCharacter(self):
        return(self.queue.pop(-1)) # remove and return the  last index