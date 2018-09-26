
#Procedure for Option
def option():
    repeat = input("Do You Want to Use the Refrigerator? Y/N ").upper()
    if repeat == "Y":
        action()
    elif repeat == "N":
        print("Refrigerator Closed")
    else:
        print("Y/N only")
        option()


#Procedure for Action
def action():
    choose = input("Choose an Action : PUT/TAKE/VIEW ").upper()
    if choose == "PUT":
        put()
    elif choose == "TAKE":
        take()
    elif choose == "VIEW":
        view()
    else:
        print("PUT/TAKE/VIEW only")
        action()

def view():
    for i in range(len(fridge)):
        print("----------\n")
        for j in fridge[i]:
            print(j, ':',fridge[i][j],"\n")
        print("----------\n")
    option()

#Procedure for Put
def put():
    pick = input("Pick Space : TOP/MIDDLE/BOTTOM ").upper()
    if pick == "TOP":
        item = input("What Do You Want to Put In : ")
        volume = int(input("Volume of Item : "))
        fridge[0][item] = volume
        print (item,"is in the Fridge")
        sum=0
        for i in range (len(fridge[0])):
            sum = sum + fridge[0][item]
        available=15-sum
        print("Available Space in the Top Part of the Fridge is,",available)
        if available < 0:
            print("Top Part of the Fridge is Full!")
            fridge[0].pop(item)
            sum = 0
            for i in range(len(fridge[0])):
                sum = sum + fridge[0][item]
            available = 15 - sum
            print("Available Space in the Top Part of the Fridge is,", available)
        option()
    elif pick == "MIDDLE":
        item = input("What Do You Want to Put In : ")
        volume = int(input("Volume of Item : "))
        fridge[1][item] = volume
        print(item,"is in the Fridge")
        sum = 0
        for i in range (len(fridge[1])):
            sum = sum + fridge[1][item]
        available=15-sum
        print("Available Space in the Middle Part of the Fridge is", available)
        if available < 0:
            print("Middle Part of the Fridge is Full!")
            fridge[1].pop(item)
            sum=0
            for i in range(len(fridge[1])):
                sum = sum + fridge[1][item]
            available = 15 - sum
            print("Available Space in the Middle Part of the Fridge is", available)
        option()
    elif pick == "BOTTOM":
        item = input("What Do You Want to Put In : ")
        volume = int(input("Volume of Item : "))
        fridge[2][item] = volume
        print(item, "is in the Fridge")
        sum = 0
        for i in range(len(fridge[2])):
            sum = sum + fridge[2][item]
        available = 15 - sum
        print("Available Space in the Bottom Part of the Fridge is", available)
        if available < 0:
            print("Bottom Part of the Fridge is Full!")
            fridge[2].pop(item)
            sum=0
            for i in range(len(fridge[2])):
                sum = sum + fridge[2][item]
            available = 15 - sum
            print("Available Space in the Bottom Part of the Fridge is", available)
        option()
    else:
        print("TOP/MIDDLE/BOTTOM only")
        put()


#Procedure for Take
def take():
    pick=input("Pick Space : TOP/MIDDLE/BOTTOM ").upper()
    if pick == "TOP":
        item = input("What Do You Want to Take Out : ")
        if item not in fridge[0]:
            print("Item doesn't exist.")
            option()
        else:
            fridge[0].pop(item)
            print(item,"is out of the Fridge")
            sum=0
            for i in range(len(fridge[0])):
                for i in fridge[0].values():
                    sum = sum + i
            available = 15 - sum
            print("Available Space in the Top Part of the Fridge is", available)
            option()

    elif pick == "MIDDLE":
        item = input("What Do You Want to Take Out : ")
        if item not in fridge[1]:
            print("Item doesn't exist.")
            option()
        else:
            fridge[1].pop(item)
            print(item,"is out of the Fridge")
            sum=0
            for i in range(len(fridge[1])):
                for i in fridge[1].values():
                    sum = sum + i
            available = 15 - sum
            print("Available Space in the Middle Part of the Fridge is", available)
            option()
    elif pick == "BOTTOM":
        item = input("What Do You Want to Take Out : ")
        if item not in fridge[2]:
            print("Item doesn't exist.")
            option()
        else:
            fridge[2].pop(item)
            print(item, "is out of the Fridge")
            sum = 0
            for i in range(len(fridge[2])):
                for i in fridge[2].values():
                    sum = sum + i
            available = 15 - sum
            print("Available Space in the Bottom Part of the Fridge is", available)
            option()

    else:
        print("TOP/MIDDLE/BOTTOM only")
        take()


#Main program
print("Welcome to the Refrigerator!")
top = {}
mid = {}
bottom = {}

fridge = [top,mid,bottom]
option()
