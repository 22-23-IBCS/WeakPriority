import random

class House:
    def __init__(self):
        self.rating = random.randint(1, 10)

    def getRating(self):
        return self.rating

def greedyPath(m, num):
    #block1
    bestHouses = []
    houses = []
    coords = []
    #for i in range 5 and j in range five makes ai(5 across) and j(5 down) 5x5
    for i in range(5):
        for j in range(5):
            houses.append(m[i][j])
            coords.append([i,j])
    #for loop to pull outbest house from list of houses because need to sort the house list form best to worst
    for i in range(25):
        maxHval = 0
        maxHcoord = [0,0]
        
        for pos in range(len(houses)):
            if houses[pos] > maxHval:
                maxHval = houses[pos]
                maxHcoord = coords[pos]
        bestHouses.append(maxHcoord)
        houses.remove(maxHval)
        coords.remove(maxHcoord)


    #loop everything 25 times(for loop)
    #block 2
    for i in range(len(bestHouses)):
        p = []

        start = bestHouses[i]
        x = start[0]
        y = start[1]
        pVal = m[x][y]

        p.append(start)
        

        for i in range(num - 1):
          

            neighbors = [[x+1,y], [x-1,y], [x,y+1], [x, y-1]]
            bad = []
            for n in neighbors:
                if (n[0] > 4) or (n[0] < 0):
                    bad.append(n)
                elif (n[1] > 4) or (n[1] < 0):
                    bad.append(n)
                if n in p:
                    bad.append(n)

            for b in bad:
                neighbors.remove(b)
            if len(neighbors) == 0:
                break

            toBreak = False             
            for h in bestHouses:
                if toBreak:
                    break
                for n in neighbors:
                    if n == h:
                        nextHouse = n
                        break

            p.append(nextHouse)
            x = nextHouse[0]
            y = nextHouse[1]
            pVal = pVal + m[x][y]
            

        return pVal, p
    return 0, [[0,0]]
            
            


def main():
    
    m = [[], [], [], [], []]
    for l in m:
        
        for i in range(5):
            h = House()
            l.append(h.getRating())
    for i in range(5):
        print(m[0][i], m[1][i], m[2][i], m[3][i], m[4][i])

    num = int((input("How many houses?\n")))  
    
    total = 0
    for i in range(5):
        for j in range(5):
            total = total + m[i][j]

    average = total/25

    pVal, p = greedyPath(m, num)
   
    

    print(p)

    print("average value in path: " + str(pVal/num))
    print("average value in neighborhood: " + str(average))



if __name__=="__main__":
    main()
