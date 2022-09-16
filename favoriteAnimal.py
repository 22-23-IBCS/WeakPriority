        
class Desk:

    def __init__(self, col, mat):
        self.height = 3
        self.width = 6
        self.color = col
        self.material = mat
        
    def getColor(self):    
        return self.color
    
    def setColor(self, col):
        self.color = col

def main():
    print("Created instances:")
    desk1 = Desk("brown", "wood")
    desk2 = Desk("purple", "metal")
    col = desk1.getColor()
    print("Desk 1 original color: " + col)
    #print("Desk 1 material: " + desk1.getMaterial() Wasn't sure if I needed this, I know I would need to set def getMaterial and setMaterial
    desk1.setColor("pink")
    print("Desk 1 color change: " + desk1.getColor())
    print("Desk 2 color: " + desk2.getColor())

if __name__ == "__main__":
        main()
