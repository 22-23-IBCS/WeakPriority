import random
import math

def prob1(x, y, z):
    mean = (x + y + z)/3
    if x < y:
        if y < z:
            median = y
        elif x < z:
            median = z
        else:
            median = x
    else:
        if x < z:
            median = x
        elif y < z:
            median = z
        else:
            median = y
    return mean, median

def prob2(randNum):
    if randNum%2 == 0 or randNum%3 == 0 or randNum%5 == 0:
        return randNum, True
    else:
        return randNum, False

def prob3():
    L=[]
    for i in range(10):
        num = random.randint(1, 50)
        L.append(num)
    max_ = L[0]
    min_ = L[0]
    for elem in L:
        if elem>max_:
            max_ = elem
        if elem<min_:
            min_ = elem       
    range_ = max_ - min_

    return max_, min_, range_

#didnt know how to do this, asked a friend, not finished
def prob4(x, y):
    L=[x, y]
    r = (math.sqrt(L[x]*L[x])+math.sqrt(L[y]*L[y]))
    feta = math.asin(r)
         
    return r, feta 


def prob5(name):
    
    #too much work to add capitals. I know there is a way to make them all lowercase but I forgot it
    scrabblePoints = {"a" : 1, "b" : 3, "c" : 3, "d" : 2, "e" : 1, "f" : 4, "g" : 2, "h" : 4, "i" : 1, "j" : 8, "k" : 5, "l" : 1, "m" : 3, "n" : 1, "o" : 1, "p" : 3, "q" : 10, "r" : 1, "s" : 1, "t" : 1, "u" : 1, "v" : 4, "w" : 4, "x" : 8, "y" : 4, "z" : 10}
    value = 0
    for i in range(len(name)):
        value = value + scrabblePoints.get(name[i])
    return value
        
                
    

def main():

    print(prob1(0, 10, 8))
    print(prob2(random.randint(1, 100)))
    print(prob3())
    print(prob4(1, 2))
    print(prob5("joseph"))
    
 
if __name__ == "__main__":
    main()
