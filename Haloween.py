import random

class House:

    
    def __init__(self):
        self.neighborhood = [[],[],[],[],[]]
        for l in self.neighborhood:
            for i in range(5):
                l.append(random.randint(1, 10))

    def getHouse(self, x, y):
        return self.neighborhood[x][y]

    def getNeighborhood(self):
        return self.neighborhood
    
    
        



def main():
    houses = House()
    for x in range(len(houses.getNeighborhood())):
        for y in range(len(houses.getNeighborhood()[x])):#length of list at spot x
            print(houses.getNeighborhood()[x][y])
    print("break 1")
    for x in range(len(houses.getNeighborhood())):
        l = []
        l.append(houses.getNeighborhood()[x][0])
        l.append(houses.getNeighborhood()[x][1])
        l.append(houses.getNeighborhood()[x][2])
        l.append(houses.getNeighborhood()[x][3])
        l.append(houses.getNeighborhood()[x][4])
        x = x+1
        print(l)
    print("break 2")
    maximum = max(l)
    for x in range(0,4): #Find starting position(biggest value)
        if maximum == l[x][0]:
            yPos = x
            break
        if maximum == l[x][1]:
            yPos = x
            break
        if maximum == l[x][2]:
            yPos = x
            break
        if maximum == l[x][3]:
            yPos = x
            break
        if maximum == l[x][4]:
            yPos = x
            break
    print(yPos)
        
        



















'''


    maximum = max(l)
    print(maximum)
    print("break 3")
    for i in range (0,len(l)):
        if (l[i]==maximum):
            break
    if(i<=4):
        x=0
        y=i
    if(4<i<=9):
        x=1
        y=i-5
    if(9<i<=14):
        x=2
        y=i-10
    if(14<i<=19):
        x=3
        y=i-15
    if(19<i<=24):
        x=4
        y=i-20
    print("break 4")
    print(i)
    print(x,y)
    print(houses.getHouse(x,y))
    
            
    
'''
     

if __name__=="__main__":
    main()
