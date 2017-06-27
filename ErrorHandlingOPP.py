from os import system
class ErrorChecking():
    temp=None

    def yesNo(self,text):
        try:
            self.temp = (raw_input(text[:-2]+" would you like to enter value yes or no:")).lower()

        except:
            TypeError
            system("say Invalid Type Entry")
            self.yesNo(text)

        if self.temp == "yes" or self.temp == "no":
            choice = self.temp

        else:
            system("say Invalid Entry")
            self.yesNo(text)
            choice = self.temp

        return choice

    def checkValue(self,text,element,optional=None,olist=None):
        if not(optional==None):

            value=ErrorChecking().yesNo(text)
            if(value=='no'):
                self.temp = olist[optional]
                return self.temp

        try:
            self.temp = input(text)
            value = self.temp
        except:
            TypeError
            system("say Invalid Entry, Please try again")
            self.checkValue(text, element,optional,olist)
            value=self.temp
        return value

    @staticmethod
    def decimalValue(value,text,element):
        print value
        if (0.0 <= value <= 100.0):
            if "Downpay" in element:
                return value
            else:
                value = calucations().convertDecimal(value)
                return value
        else:
            print value
            system("say That is not a percentage\nPlease try to re-enter value: ")
            ErrorChecking().checkValue(text,element)

    def CheckChar(self, text):
        try:
            self.temp = raw_input(text).lower()
            value = self.temp
        except:
            TypeError
            system("say Invalid Input, please try again!")
            self.CheckChar(text)
            value = self.temp
        return value



class calucations(object):

    def convertPercentage(self,num):
        return ((num - 1) * 100)

    def convertDecimal(self,num):
        return ((float(num)/100)+1)

    def calculate(self,func,*args,**kwargs):
        def PayPlan():
            print "Monthly payment: ",
            return func
        return PayPlan

    def priceValue(self,func,class_value):
        if ('Purchases.car' in str(class_value.__class__)):
            item="car"
        elif ('Purchases.house' in str(class_value.__class__)):
            item="house"
        else:
            item =" "
        system("say Calculating the expense for " +item)
        return self.calculate(func, class_value)