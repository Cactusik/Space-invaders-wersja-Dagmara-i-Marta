def setup():
    size(700, 500)
    background(74, 35, 90)

def draw():
    alien = square(30, 20, 55)
    fill(255, 0, 0)

    print(mouseX, mouseY)
    
class Wrog():
    
    def __init__(self, x,y):
        
        self.zycie = 2
        self.x = x
        self.y = y
        self.ruch = 1
        self.speed = 3
    
        
    def strac_zycie(self, zycie):
        self.zycie -= 1
        
    def ruch(self):
        self.x += self.ruch*self.speed
    
        
        
        


    
