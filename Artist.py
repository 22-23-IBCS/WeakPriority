import turtle

class Artist:

    def __init__(self, t):
        self.t = t

    def Triangle(self, size = 50):
        for i in range(3):    
            self.t.right(120)
            self.t.forward(size)

    def Square(self, size = 100):
        for i in range(4):
            self.t.right(90)
            self.t.forward(size)

    def Polygon(self, size):
        #not exactly sure how to add to the set integers in a for loop
        self.t.left(60)
        self.t.forward(80)
        self.t.left(70)
        self.t.forward(90)
        self.t.left(40)
        self.t.forward(60)
        self.t.left(50)
        self.t.forward(70)
        self.t.left(102)
        self.t.forward(166)


    def Star(self, size = 100):
        for i in range(5):
            self.t.forward(100)
            self.t.right(144)

    def Wink(self, size = 100):
        self.t.left(38)
        self.t.forward(50)
        self.t.penup()
        self.t.goto(230, -25)
        self.t.pendown()
        self.t.left(90)
        self.t.forward(50)
        self.t.penup()
        self.t.goto(135, -50)
        self.t.right(180)
        self.t.pendown()
        for i in range(180):
            self.t.left(1)
            self.t.forward(1)

    def Circle(self, size = 50):
        for i in range(360):
            self.t.left(1)
            self.t.forward(1)

    def X(self, size = 200):
        self.t.left(45)
        self.t.forward(70)
        self.t.penup()
        self.t.goto(-200, 200)
        self.t.pendown()
        self.t.left(90)
        self.t.forward(70)
                      

    def move(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

        

def main():
    Page = turtle.Screen()
    Page.bgcolor = ("cyan")
    Page.title("turtle drawing")
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(0)
    art = Artist(t)
    
    art.move(-150, -150)
    art.Triangle(200)
    art.move(-200, 200)
    art.Square(50)
    art.move(150, 150)
    art.Polygon(80)
    art.move(150, -150)
    art.Star(100)
    art.move(150, 0)
    art.Wink(50)
    art.move(-200, 150)
    art.X(50)
    art.move(0, 0)
    art.Circle(100)
    

if __name__ == "__main__":
    main()
