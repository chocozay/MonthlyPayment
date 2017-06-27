from ErrorHandlingOPP import ErrorChecking
from ErrorHandlingOPP import calucations
from P_Track import PurchaseTracker
import Purchases
import os


def decision():
    item = ['Car','House']

    text = "Enter 1 to get monthly payment for new car\n" \
           "Enter 2 to get monthly payment for new house\n" \
           "Enter 3 to get list of all purchases considered\n" \
           "Enter 4 to search for particular purchase\n" \
           "Enter 5 to search for particular component of a purchase\n" \
           "Enter 6 to exit\n" \
           "Please enter a number: "

    # os.system("say Enter 1 to get payment for new car,Enter 2 to get payment for new house,Enter 3 to get list of all items,Enter 4 to search for particular purchase,Enter 5 to search for particular component of a purchase,Enter 6 to exit,Please enter a number: ")

    selection = ErrorChecking().checkValue(text,element="")
    print
    if(selection==1 or selection== 2):
        if(selection==1 or selection==2):
            os.system("say You have enter "+str(selection)+", please enter in the following information to receive valid monthly "+item[selection-1]+" payments amount")
        else:
            os.system("say You have enter " + str(selection))

    if (not(1<=selection<=6) or type(selection)== float):
        os.system("say Invalid Entry, please try again!")

        decision()
    elif(selection==1):
        newCar = Purchases.car.setCar()
        newCar.MonthlyPayments = calucations().priceValue(newCar.carMonthly(newCar),newCar)()
        # os.system("say You will be paying"+"{:,.2f}".format(newCar.MonthlyPayments)+" dollars every month!")
        print "{:,.2f}".format(newCar.MonthlyPayments)
        Purchases.purchase.purchasesConsidered.append(newCar)
        Purchases.car.purchasesConsidered.append(newCar)
        text = "Please enter name of car: "
        PurchaseTracker().add(ErrorChecking().CheckChar(text),newCar)
    elif(selection==2):
        newHouse = Purchases.house.setHouse()
        newHouse.MonthlyPayments = calucations().priceValue(newHouse.houseMonthly(newHouse),newHouse)()
        # os.system("say You will be paying"+"{:,.2f}".format(newHouse.MonthlyPayments)+" dollars every month!")
        print "{:,.2f}".format(newHouse.MonthlyPayments)
        Purchases.purchase.purchasesConsidered.append(newHouse)
        Purchases.house.purchasesConsidered.append(newHouse)
        text = "Please enter name of House: "
        PurchaseTracker().add(ErrorChecking().CheckChar(text),newHouse)
    elif(selection==3):
        PurchaseTracker().displayAll()
    elif(selection==4):
        text="Enter the name correlating to what you want information on or enter no to exit:"
        value_check=ErrorChecking().CheckChar(text)
        while(PurchaseTracker().doesExist(value_check) and value_check!= "no"):
            print "Name does not exist,if you would like to exit enter no"
            value_check = ErrorChecking().CheckChar(text)
        if(value_check=="no"):
            pass
        else:
            PurchaseTracker().displaySec(value_check)
    elif(selection==5):
        print "Five was entered"

    return selection




flag = True
# os.system("say Welcome to the monthy payment calculator!")
carA=Purchases.car(21000,800)
houseA=Purchases.house(100000,800)
carA.carMonthly= calucations().priceValue(carA.carMonthly(carA),carA)()
houseA.houseMonthly= calucations().priceValue(houseA.houseMonthly(houseA),houseA)()
text = "bob"
PurchaseTracker().add(text,houseA)
text = "rob"
PurchaseTracker().add(text,carA)
PurchaseTracker().displayAll()

while(flag):

    value =decision()
    if not(value==6):
        if(ErrorChecking().yesNo(text="Would you like to check something else, yes or no: ") == "no"):
            flag = False
    else:
        flag =False
    print
os.system("say Thank you again and have a great day!")
