# Node class 
class node: 
   
    # Function to initialize the node object 
    def __init__(self, x, y): 
        self.location =[x,y]  
        self.next = None                  
        self.up = None
        is_wall =False
        self.prev = None
   
# Linked List class 
