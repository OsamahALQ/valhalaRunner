import random 


print("Hello, GAMER! Welcome to the Valhala Runner Loot Box Pruchasing System.")
name=input("First, What is your name: ")
print("Welcome! " + name)

orders = 0
total = 0
item1=0
item2=0
item3=0
orderslist = []
finalorder = []
prices = []
boxtype = []

def print_menu():
    print("Please select a loot box from the menu below")
    print("1-[Common] Golden Box (2.99)")
    print("2-[Rare] Warrior Temple (4.99)")
    print("3-[Epic] Valhala (9.99)")
    print("4-Complete Purchase")

def receipt (name,item,price,Selection):
    global orders
    global total
    global prices
    global item1
    global item2
    global item3
  
    boxNumber=int(input("How many " + item + "(" + str(price) +") would you like?  " ))
    total = total + (boxNumber*price)
    if Selection == "1":
        if finalorder.count(item) == 1:
            item1 = item1 + boxNumber
        else: 
            orders = orders + 1
            finalorder.append(item)
            prices.append(price)
            item1 = item1 + boxNumber
    elif Selection == "2":
        if finalorder.count(item) == 1:
            item2 = item2 + boxNumber
        else:
            orders = orders + 1
            finalorder.append(item)
            prices.append(price)
            item2 = item2 + boxNumber
    elif Selection == "3":
        if finalorder.count(item) == 1:
            item3 = item3 + boxNumber
        else:
            orders = orders + 1
            finalorder.append(item)
            prices.append(price)
            item3 = item3 + boxNumber

 
def final_receipt(name):
    global orderslist
    global boxtype
    if "Golden Box" in finalorder:
        orderslist.insert(finalorder.index("Golden Box"),item1)
        boxtype.insert(finalorder.index("Golden Box"),"common")   
    if "Warrior Temple" in finalorder:
        orderslist.insert(finalorder.index("Warrior Temple"),item2)
        boxtype.insert(finalorder.index("Warrior Temple"),"rare")
    if "Valhala" in finalorder:
        orderslist.insert(finalorder.index("Valhala"),item3)
        boxtype.insert(finalorder.index("Valhala"),"epic")
    print("Thanks, {}! Here is your receipt:".format(name))
    print("-----------------------------------------------")
    for x in range(orders):
        print('{}x {}  ({})'.format((orderslist[x]),str(finalorder[x]),str(prices[x])))
    print("-----------------------------------------------")
    print('Total cost: {:.2f}'.format(total))
    print("Thank you! Good luck, gamer!")
    print(" ")
    print(" ")
   
    
    
    print("Time to Open Boxes!")
    print("--------------------------")
    for x in range(orders):
        open_box(orderslist[x],finalorder[x])

    while(True):
        Exit= input("press e to quit: ")
        if Exit == "e":
            quit()


def open_box(number_boxes,type):
    rand = random.random()
    for i in range(number_boxes):
        print("Opening " + str(boxtype[finalorder.index(type)] +" box " + str(i)))
        for x in range(3):
            rand = random.random()

            if type=="Golden Box":

                if rand<=0.8:
                    print("     Its common item!")
                elif rand<=0.95:
                    print("     It's rare item!")
                else:
                    print("     It's epic item!")
            
            if type=="Warrior Temple":
                if rand<=0.5:
                    print("     It's common item!")
                elif rand<=0.9:
                    print("     It's rar item!")
                else:
                    print("     It's epic item!")
          
            if type=="Valhala":
                if rand<=0.3:
                    print("     It's common item!")
                elif rand<=0.8:
                    print("     It's rare item!")
                else:
                    print("     It's epic item!")



print_menu()
menu=True
while menu:
    Selection=input("your selection: ")
    if Selection=="1":
        item = "Golden Box" 
        price = 2.99   
        receipt(name,item,price,Selection)
    elif Selection=="2":
        item = "Warrior Temple"
        price = 4.99
        receipt(name,item,price,Selection)
    elif Selection=="3":
        item = "Valhala"
        price = 9.99
        receipt(name,item,price,Selection)
    elif Selection == "4":
        final_receipt(name)
    else:
        menu1=print("Error: That was not a valid seletion. Please enter a number between 1-3")
    print_menu()