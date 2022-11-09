from graphics import *

class Button(Rectangle):

    def __init__(self, win, p1, p2, color, text):
        super().__init__(p1, p2)
        super().draw(win)
        super().setFill(color)

        self.minX = p1.getX()
        self.maxX = p2.getX()
        self.minY = p1.getY()
        self.maxY = p2.getY()

        self.text = Text(Point((self.minX + self.maxX)/2, (self.minY + self.maxY)/2), text)
        self.text.draw(win)

    def isClicked(self, p):
        x = p.getX()
        y = p.getY()
   
        if x > self.minX:
            if x < self.maxX:
                if y > self.minY:
                    if y < self.maxY:
                        return True
        return False

class Quit(Button):
    def __init__(self, win, p1, p2):
        super().__init__(win, p1, p2, "red", "Quit")

                
            
    
    
def main():

    win = GraphWin("Button Example", 500, 500)
    B = Button(win, Point(300, 100), Point(400, 175), "cyan", "Click Me")
    Quit = Button(win, Point(300, 200), Point(400, 275), "red", "Quit")

    i = 0
    while True:
        m = win.getMouse()

        if B.isClicked(m):
            C1 = Circle(Point(250, 250), 10)
            C2 = Circle(Point(200, 250), 10)
            C3 = Circle(Point(225, 350), 50)
            
            C1.draw(win)
            C2.draw(win)
            C3.draw(win)

        if Quit.isClicked(m):
            win.close()
            break

    
if __name__ == "__main__":
    main()
