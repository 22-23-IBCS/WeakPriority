

class groceryStore:
    def __init__(self):
        self.inventory = ["Apple", "Orange", "Pizza", "Pasta", "Chicken", "Beef", "Chips", "Bread", "Ice cream", "Cookies"] 
        self.prices = {"Apple" : 1.50,
                                      "Orange" : 2.00,
                                      "Pizza" : 6.50,
                                      "Pasta" : 4.25,
                                      "Chicken" : 5.00,
                                      "Beef" : 8.00,
                                      "Chips" : 1.00,
                                      "Bread" : 3.00,
                                      "Ice cream" : 4.00,
                                      "Cookies" : 100.00}
        self.storeName = "Metropolitan Market"
        self.manName = "Darrel"

    def getProducts(self):
        return self.inventory
    def getPrices(self):
        return self.prices
    def getstoreName(self):
        return self.storeName

    def speakManager(self):
        return ("Hi, welcome to " + self.storeName + ", my name is " + self.manName)

#def inventory_list(self):
    
#num = length of list
    #def buy(grocery_list, num):
        #for i in num:
            #total = 0
            #item_price = item_price.getProducts()
    
    





def main():
    grocery1 = groceryStore()
    grocery1.getProducts()
    grocery1.getPrices()
    toBuy = []
    total = 0
    print(grocery1.getstoreName() + "\n---------------------")


    choice = int(input("What would you like to do?\nType 1 to shop\nType 2 to talk to the manager\n"))
    if choice == 1:
        print("items sold:\nApple, Orange, Pizza, Pasta, Chicken, Beef, Chips, Bread, Ice cream, Cookies") 
        while True:
            result = input("What would you like to buy? enter \"stop\" if done.\n")
            if result == "stop":
                break
            #elif result not in(list_inventory):
                #print("sorry, we do not have that here")
            else:
                many = int(input("How many do you want?\n"))
                price_per = int(grocery1.getPrices().get(result))
                total = total + price_per*many
                toBuy.append(result)
        print("your total is: $" + str(total))
    if choice == 2:
        print(grocery1.speakManager())




            
if __name__ == "__main__":
    main()
