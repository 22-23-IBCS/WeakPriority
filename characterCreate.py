from graphics import*
from Button import*



def main():
    win = GraphWin("Charater Creation", 800, 900)

    B1 = Button(win, Point(650, 50), Point(750, 125), "salmon", "Face")
    
    B2 = Button(win, Point(650, 150), Point(750, 225), "salmon", "Big Eyes")
    B3 = Button(win, Point(650, 250), Point(750, 325), "salmon", "Small Eyes")

    B4 = Button(win, Point(650, 350), Point(750, 425), "salmon", "Mouth 1")
    B5 = Button(win, Point(650, 450), Point(750, 525), "salmon", "Mouth 2")

    B6 = Button(win, Point(650, 550), Point(750, 625), "salmon", "Nose 1")
    B7 = Button(win, Point(650, 650), Point(750, 725), "salmon", "Nose 2")



    Face = Oval(Point(150, 50), Point(550, 550))

    bigEye1 = Circle(Point(350, 250), 40)
    bigEye2 = Circle(Point(450, 250), 40)
    smallEye1 = Circle(Point(350, 250), 20)
    smallEye2 = Circle(Point(450, 250), 20)

    Mouth1_pt1 = Line(Point(350, 450), Point(400, 450))
    Mouth1_pt2 = Line(Point(350, 435), Point(350, 465))
    Mouth1_pt3 = Line(Point(400, 435), Point(400, 465))

    Mouth2_pt1 = Line(Point(325, 450), Point(350, 425))
    Mouth2_pt2 = Line(Point(375, 450), Point(350, 425))

    #Nose1_pt1 = Line(Point(350

    
    
    
    Q = Quit(win, Point(650, 775), Point(750, 875))


    while True:
        m = win.getMouse()
        if B1.isClicked(m):
            Face.undraw()
            Face.draw(win)

        if B2.isClicked(m):
            bigEye1.undraw()
            bigEye2.undraw()
            smallEye1.undraw()
            smallEye2.undraw()
            bigEye1.draw(win)
            bigEye2.draw(win)

        if B3.isClicked(m):
            bigEye1.undraw()
            bigEye2.undraw()
            smallEye1.undraw()
            smallEye2.undraw()
            smallEye1.draw(win)
            smallEye2.draw(win)

        if B4.isClicked(m):
            Mouth1_pt1.undraw()
            Mouth1_pt2.undraw()
            Mouth1_pt3.undraw()
            Mouth2_pt1.undraw()
            Mouth2_pt2.undraw()
            Mouth1_pt1.draw(win)
            Mouth1_pt2.draw(win)
            Mouth1_pt3.draw(win)

        if B5.isClicked(m):
            Mouth1_pt1.undraw()
            Mouth1_pt2.undraw()
            Mouth1_pt3.undraw()
            Mouth2_pt1.undraw()
            Mouth2_pt2.undraw()
            Mouth2_pt1.draw(win)
            Mouth2_pt2.draw(win)
            

            
        if Q.isClicked(m):
            break
    win.close()
        


if __name__ == "__main__":
    main()
