from graphics import *
from Button import *


def main():

    win = GraphWin("madlib", 800, 600)

    N1Text = Text(Point(80, 100), "enter a noun")
    N1Text.draw(win)

    Noun1 = Entry(Point(200, 100), 20)
    Noun1.draw(win)

    N2Text = Text(Point(80, 200), "enter a noun")
    N2Text.draw(win)

    Noun2 = Entry(Point(200, 200), 20)
    Noun2.draw(win)

    V1Text = Text(Point(80, 300), "enter a verb")
    V1Text.draw(win)

    Verb1 = Entry(Point(200, 300), 20)
    Verb1.draw(win)

    A1Text = Text(Point(75, 400), "enter an adjective")
    A1Text.draw(win)

    Adj1 = Entry(Point(200, 400), 20)
    Adj1.draw(win)

    E1Text = Text(Point(70, 500), "enter an exclamation")
    E1Text.draw(win)

    Excl1 = Entry(Point(200, 500), 20)
    Excl1.draw(win)

    B = Button(win, Point(400, 500), Point(520, 580), "tomato", "generate")

    Q = Quit(win, Point(650, 750), Point(750, 800))


    while True:

        m = win.getMouse()

        if B.isClicked(m):
            noun1 = Noun1.getText()
            noun2 = Noun2.getText()
            verb1 = Verb1.getText()
            adj1 = Adj1.getText()
            excl1 = Excl1.getText()
            win.close
            storywin = GraphWin("Story", 800, 600)
            story = Text(Point(200, 200), "Once upon a time " + noun1 + " was " + verb1 + " and saw " + noun2 + "." + noun1 " Was " + adj1 + " and yelled: " + excl1 + "!")
            story.draw(storywin)

            if Q.isClicked(m):
                break
    storywin.close()


    
            

        

if __name__ == "__main__":
    main()
