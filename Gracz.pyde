def setup():
    size(700, 500)
    background(74, 35, 90)
    
def draw():
    statek = circle(335, 450, 55)
    fill(241, 196, 15)
    
    print(mouseX, mouseY)


class Gracz():
    
    def __init__(self,x,y):
        
        # x i y - pozycja
        
        self.zycie = 3
        self.x = x
        self.y = y
        self.ruch = ruch
        self.pokonani_wrogowie = 0
        
    def pokonaj_wroga(self):
        self.pokonani_wrogowie += 1
        print("Wrog pokonany!")
        return self.pokonani_wrogowie
    
    def strac_zycie(self,zycie):
        self.zycie -= 1
        
    def set_pokonani_wrogowie(self,ilosc):
        self.pokonani_wrogowie = ilosc
