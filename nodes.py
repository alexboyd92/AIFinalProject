# Node class 
class Node: 
   
    # Function to initialize the node object 
    def __init__(self, x, y): 
        self.location = [x,y]  
        self.next = None                  
        self.up = None
        self.right = None
        self.down = None
        self.left = None
        is_wall = False
        self.prev = None

   
 
