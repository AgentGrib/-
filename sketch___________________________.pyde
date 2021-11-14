x1 = 500
y1 = 250
x2 = 500
y2 = 250
x3 = 500
y3 = 250
def setup ():  
    size (1000,500)
    frameRate (50)
def draw ():
    global x1,y1
    global x2,y2
    global x3,y3
    fill (0,255)
    triangle (x1,y1,x2,y2,x3,y3)
    y1 = y1-1
    x2 = x2+1
    y2 = y2+1
    x3 = x3-1
    y3 = y3+1
    
    
    
    
    
    
    
    
