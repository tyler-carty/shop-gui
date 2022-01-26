from tkinter import *
import csv
import time

shoppinglist = []
totalc = 0


##----------------------------------------------------------------------------------------------


def shop():
    
    window4 = Tk()
    window4.geometry("510x800+1335+100")
    window4.title("Shop")
    window4.configure(background = "white")

    label4 = Label(window4, text = "Welcome to the Item Shop", bg = "gray", fg = "white")
    label4.place(x = 155, y = 15, width = 200, height = 30)

    label5 = Label(window4, text = "Enter Barcode:", bg = "gray", fg = "white")
    label5.place(x = 100, y = 70, width = 90, height = 30)

    label5b = Label(window4, text = "Enter Quantity:", bg = "gray", fg = "white")
    label5b.place(x = 100, y = 110, width = 90, height = 30)

    label6 = Label(window4, text = "Available Items:", bg = "gray", fg = "white")
    label6.place(x = 60, y = 160, width = 90, height = 30)

    label7 = Label(window4, text = "Cost:", bg = "gray", fg = "white")
    label7.place(x = 160, y = 160, width = 90, height = 30)

    label8 = Label(window4, text = "Barcode:", bg = "gray", fg = "white")
    label8.place(x = 260, y = 160, width = 90, height = 30)

    label9 = Label(window4, text = "Stock Level:", bg = "gray", fg = "white")
    label9.place(x = 360, y = 160, width = 90, height = 30)

    label10 = Label(window4, text = "Your Current Shopping List:", bg = "gray", fg = "white")
    label10.place(x = 150, y = 350, width = 210, height = 30)

    label11 = Label(window4, text = "If the quantity chosen is larger than the quantity we have in stock \n then you will only be billed for and given the amount we have in stock.", bg = "gray", fg = "white")
    label11.place(x = 55, y = 655, width = 400, height = 40)

    ItemEntry = Entry(window4, text = "")
    ItemEntry.place(x = 210, y = 70, width = 90, height = 30)

    QuanEntry = Entry(window4, text = "")
    QuanEntry.place(x = 210, y = 110, width = 90, height = 30)

    ItemList = Listbox(window4)
    ItemList.place(x = 60, y = 200, width = 90, height = 130)

    CostList = Listbox(window4)
    CostList.place(x = 160, y = 200, width = 90, height = 130)

    BarcodeList = Listbox(window4)
    BarcodeList.place(x = 260, y = 200, width = 90, height = 130)

    StockList = Listbox(window4)
    StockList.place(x = 360, y = 200, width = 90, height = 130)

    ShoppingListList = Listbox(window4)
    ShoppingListList.place(x = 60, y = 450, width = 390, height = 170)

    button10 = Button(window4, text = "Add Item", bg = "gray", fg = "white", command = lambda: ShoppingList(window4,ItemEntry,QuanEntry))
    button10.place(x = 320, y = 90, width = 90, height = 30)

    button11 = Button(window4, text = "Update Table", bg = "gray", fg = "white", command = lambda: ShowList(window4,ShoppingListList,ItemEntry,QuanEntry))
    button11.place(x = 100, y = 400, width = 90, height = 30)

    button11 = Button(window4, text = "Clear Table", bg = "gray", fg = "white", command = lambda: ClearShoppingListList(ShoppingListList))
    button11.place(x = 320, y = 400, width = 90, height = 30)

    button12 = Button(window4, text = "Exit Shop", bg = "gray", fg = "white", command = lambda: ExitShop(window4))
    button12.place(x = 100, y = 730, width = 120, height = 30)

    button13 = Button(window4, text = "Clear Shopping List", bg = "gray", fg = "white", command = ClearShoppingList)
    button13.place(x = 290, y = 730, width = 120, height = 30)

    itemsdata = readfile(open("Items.csv"))
    for item in itemsdata:
        ItemList.insert(END,item[1])
        CostList.insert(END,"£"+item[2])
        BarcodeList.insert(END,item[0])
        StockList.insert(END,item[3])


def ShoppingList(window4,ItemEntry,QuanEntry):
    
    check = 0
    itemsdata = readfile(open("items.csv"))
    
    global shoppinglist
    global totalc

    searchItem = ItemEntry.get()
    quan = QuanEntry.get()

    for item in itemsdata:
        if item[0] != searchItem:
            check = check + 1

    while check != 8:
        for item in itemsdata:
            if item[0] == searchItem:

                if int(quan) > int(item[3]):

                    quan = item[3]
                    
                    totcost = int(quan)*int(item[2])
                    item[3] = int(item[3]) - int(quan)
                    shoppinglist.append([searchItem,item[1],quan,totcost])
                    totalc = totalc + totcost
                    updateCSV(itemsdata)

                    
                elif int(quan) <= int(item[3]):

                    totcost = int(quan)*int(item[2])
                    item[3] = int(item[3]) - int(quan)
                    shoppinglist.append([searchItem,item[1],quan,totcost])
                    totalc = totalc + totcost
                    updateCSV(itemsdata)

        break

    while check == 8:
        shoppinglist.append([searchItem,"Product Not Found",quan,"0"])
        break

    ItemEntry.delete(0,END)
    QuanEntry.delete(0,END)

    window4.destroy()
    shop()
    

def ShowList(window4,ShoppingListList,ItemEntry,QuanEntry):

    global shoppinglist

    for item in shoppinglist:
        ShoppingListList.insert(END,item[2] + " x " + item[1] + " --- £" + str(item[3]))

    totalcharge = 0
    for item in shoppinglist:
        totalcharge = totalcharge + (int(item[3]))

    ShoppingListList.insert(END,"Your Total Charge Is:  £" + str(totalcharge))

def ClearShoppingListList(ShoppingListList):
    ShoppingListList.delete(0,END)

def ExitShop(window4):
    window4.destroy()

def ClearShoppingList():
    global shoppinglist
    shoppinglist = []
    print(shoppinglist)

##----------------------------------------------------------------------------------------------


def checkstock():
    window3 = Tk()
    window3.geometry("265x300+950+100")
    window3.title("Check Stock Levels")
    window3.configure(background = "white")

    label3 = Label(window3, text = "Would You Like To Check the Stocks?", bg = "gray", fg = "white")
    label3.place(x = 25, y = 15, width = 205, height = 30)

    button7 = Button(window3, text = "Yes", bg = "gray", fg = "white", command = lambda: CheckYes(window3,CheckResult))
    button7.place(x = 25, y = 55, width = 95, height = 30)

    button8 = Button(window3, text = "Exit", bg = "gray", fg = "white", command = lambda: CheckNo(window3))
    button8.place(x = 135, y = 55, width = 95, height = 30)

    button9 = Button(window3, text = "Clear Table", bg = "gray", fg = "white", command = lambda: ClearTable(CheckResult))
    button9.place(x = 52, y = 250, width = 150, height = 30)

    CheckResult = Listbox(window3)
    CheckResult.place(x = 25, y = 100, width = 205, height = 130)


def CheckYes(window3,CheckResult):
    
    itemsdata = readfile(open("Items.csv"))

    for items in itemsdata:
        if int(items[3]) <= int(items[4]):
            CheckResult.insert(END,"We Need More of: "+ items[1])
        elif int(items[3]) > int(items[4]):
            CheckResult.insert(END,"We Don't Need: "+ items[1])


def CheckNo(window3):
    window3.destroy()


def ClearTable(CheckResult):
    CheckResult.delete(0,END)
    

##----------------------------------------------------------------------------------------------


def restock():
    window2 = Tk()
    window2.geometry("400x100+450+100")
    window2.title("Restock Menu")
    window2.configure(background = "white")


    label2 = Label(window2, text = "Would You Like To Restock the Items?", bg = "gray", fg = "white")
    label2.place(x = 100, y = 15, width = 210, height = 30)


    button5 = Button(window2, text = "Yes", bg = "gray", fg = "white", command = lambda: RestockYes(window2))
    button5.place(x = 50, y = 50, width = 125, height = 30)

    button6 = Button(window2, text = "No", bg = "gray", fg = "white", command = lambda: RestockNo(window2))
    button6.place(x = 225, y = 50, width = 125, height = 30)


def RestockYes(window2):
    
    itemsdata = readfile(open("Items.csv"))

    for items in itemsdata:
        if int(items[3]) > int(items[4]):
            pass
        elif int(items[3]) <= int(items[4]):
            difference = int(items[5])-int(items[3])
            items[3] = int(items[3]) + int(difference)
            updateCSV(itemsdata)
            pass

    window2.destroy()


def updateCSV(itemsdata):
    ofile  = open('Items.csv', 'w', newline='')
    writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)

    for item in itemsdata:
        writer.writerow(item)
    
    ofile.close()

    return
    

    
def RestockNo(window2):
    window2.destroy()


def readfile(f):#this subroutine opens the file
    csvFile = csv.reader(f)#"
    tempArray = []#"
    for row in csvFile:#"
        tempArray.append(row)#"
        f.close#"
    return tempArray#
    
    
##----------------------------------------------------------------------------------------------


def exit():
    quit()


##----------------------------------------------------------------------------------------------

window = Tk()
window.geometry("250x250+100+100")
window.title("Main Menu")
window.configure(background = "white")


label1 = Label(text = "Welcome To The Main Menu", bg = "gray", fg = "white")
label1.place(x = 25, y = 25, width = 200, height = 30)


button1 = Button(text = "Enter the Shop", bg = "gray", fg = "white", command = shop)
button1.place(x = 50, y = 75, width = 150, height = 30)


button2 = Button(text = "Check Stock Levels", bg = "gray", fg = "white", command = checkstock)
button2.place(x = 50, y = 110, width = 150, height = 30)


button3 = Button(text = "Restock Items", bg = "gray", fg = "white", command = restock)
button3.place(x = 50, y = 145, width = 150, height = 30)


button4 = Button(text = "Exit the Program", bg = "gray", fg = "white", command = exit)
button4.place(x = 50, y = 180, width = 150, height = 30)

