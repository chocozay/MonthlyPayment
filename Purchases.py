from ErrorHandlingOPP import ErrorChecking
from ErrorHandlingOPP import calucations
from os import system

#Parent class for all purchases
class purchase(object):

    tax =1.09               #Initial value for tax
    interest=0.00           #Intial value for interest
    purchasesConsidered=[]  #List of all previous purchases
    temp = None             #Use for storing temporary values
    tempList = []           #Use for storing temporary lists

    def __init__(self,price=None,creditScore=None,years=1.0/12.0):
        self.price=abs(int(price))
        while not(300.0<=creditScore<=850.0):
                system("say You entered invalid credit score: "+str(creditScore))
                question = "Please enter a valid credit score:"
                creditScore= ErrorChecking().checkValue(question,element="Credit")
        self.creditScore=int(creditScore)
        if years == 0 or years == None:
            self.years = 1.0/12.0
        else:
            self.years = float(years)

    @staticmethod
    def getAttribs(TypeList,OptionalList):
        """ For creating instances of car or house car
            The parameters are: list of args for house or car and the list of kwargs which are optional values"""

        optionalValue=0     #Counter for how many optional values that can be used

        for x in TypeList:

            Text= x[2:]+": "
            OptionalText="This is optional, "+x[2:-1]+": "

            if(x[-1:]=="*"):

                value=ErrorChecking().checkValue(OptionalText,x,optionalValue,OptionalList)

                purchase.tempList.append(value)
                optionalValue+=1

            else:

                value=ErrorChecking().checkValue(Text,x)

                purchase.tempList.append(value)

    def getDownPay(self,value=None):
        try:
            if(value==None):
                value = input("Enter Down Payment amount: ")
            else:
                return int(value)
            if(value<1000 or value==None):
                system("say Down Payment can not be less than 1000")
                self.getDownPay()
            else:
                return value
        except:
            TypeError
            value=None
            print "Invalid Entry"
            self.getDownPay()

        return value


class car(purchase):
    carsConsidered=[]
    attribList = ["n price","n Credit","n Financing Years*","n Down payment amount*"]
    OList = [1.0/12.0,0]
    def __init__(self,price,creditScore,years=1.0/12.0,downPay=0):
        super(car,self).__init__(price,creditScore,years=1.0/12.0)
        if not years is None:
            self.years=years
        else:
            self.years = float(1.0/12.0)
        if not downPay is 0 or downPay<1000:
            self.downPay=self.getDownPay(downPay)
        else:
            self.downPay=downPay
        self.getInterest()

    def getInterest(self):
        print self.creditScore
        flag = False
        if(self.creditScore<=650):
            system("say Since your credit score is below 650, we require you to enter at 1000 for down payment")
        if(800< self.creditScore <=850):
            self.interest = 0.00
        elif(750< self.creditScore <=800):
            self.interest = 1.02
        elif(700< self.creditScore <=750):
            self.interest = 1.04
        elif(650< self.creditScore <=700):
            purchase.interest = 1.08
        elif(600< self.creditScore <=650):
            if(self.downPay<1000):
                self.downPay = self.getDownPay()
            self.interest = 1.12
        elif(550< self.creditScore <=600):
            if(self.downPay<1000):
                self.downPay = self.getDownPay()
            self.interest = 1.14
        elif(500< self.creditScore <=550):
            if(self.downPay<1000):
                self.downPay = self.getDownPay()
            self.interest = 1.17
        else:
            if(self.downPay<1000):
                self.downPay = self.getDownPay()
            self.interest = 1.20


    def carMonthly(self,car_class):
        return round(((car_class.price-car_class.downPay)*car_class.tax*car_class.interest)/(car_class.years*12),2)

    @classmethod
    def setCar(cls):
        purchase.getAttribs(car.attribList, car.OList)
        price, creditScore, years, downPercent = purchase.tempList
        purchase.tempList = []
        return cls(price, creditScore, years, downPercent)



class house(purchase):
    houseConsidered =[]
    attribList= ["n Price","n Credit","n Years*","f Downpay Percentage*","f Interest*"]
    OList = [1.0/12.0,20,3.81]
    downPay=0

    def __init__(self, price, creditScore, years=1.0/12.0, downPercent=20,interest=3.81):
        super(house,self).__init__(price,creditScore,years=1.0/12.0)
        self.years=years
        if not interest is 3.81:
            if not(0.0<= interest<= 100.0):
                self.interest = calucations().convertPercentage(ErrorChecking().checkValue(text="Please enter interest: ",element="interest"))
            else:
                self.interest= interest
        else:
            self.interest = 1.0384
        if not downPercent == 20:
            self.downPercent= round(float(downPercent)/100.0,2)
        else:
            self.downPercent = 0.2


    def get_downpay(self):
        self.downPay=self.price * self.downPercent

    def houseMonthly(self,house_class):
        self.get_downpay()
        print house_class.__dict__
        return round(((house_class.price - house_class.downPay) * (house_class.tax) * house_class.interest) / (12.0 * house_class.years),2)

    @classmethod
    def setHouse(cls):
        purchase.getAttribs(house.attribList,house.OList)
        price, creditScore, years, downPercent, interest = purchase.tempList
        purchase.tempList=[]
        return cls(price, creditScore, years, downPercent, interest)



def display(list):
    if not any(list):
        system("say I am sorry but there are not any purchases that have been stored!")
        return
    for cell in list:
        temp = cell.__dict__
        for index in temp.items():
            print "{} = {}".format(*index)
        print

# def displayHouse():
#     if not any(house.houseConsidered):
#         system("say I am sorry but there are not any purchases that have been stored!")
#         return
#     for cell in house.houseConsidered:
#         temp = cell.__dict__
#         for index in temp.items():
#             print "{} = {}".format(*index)
#         print


