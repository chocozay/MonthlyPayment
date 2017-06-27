from ErrorHandlingOPP import ErrorChecking
from os import system

class PurchaseTracker(object):

    ChoiceDict = {}

    # def get_comp(self,):
    def add(self,name,purchase_object):
        self.ChoiceDict.update({name: purchase_object})
        print "done"

    def get_value(self,instance_name):
        count = 0
        for index in instance_name.__dict__.keys():
            count += 1
            print "Enter ",count,"for ",index+"."

        value = ErrorChecking().checkValue(text="",element="")
        if 1<= value<= count:
            return instance_name.__dict__.keys()[value - 1],value-1
        else:
            self.get_value(instance_name)


    def Search(self, name,instance_name):
        flag = True
        for index in self.ChoiceDict.keys():
            if index == name:
                system("say "+name.title()+"has been found!")
                flag = False
                break

        if flag:
            system("say Could not find a matching name!")
            return "Could not find a matching name!"

        else:
            value = self.get_value(instance_name)
            for index in self.ChoiceDict.values()[0].__dict__.items():
                if value[0] == index[0]:
                    return "{} = {}".format(index[0],index[1])

    def displayAll(self):
        if not any(self.ChoiceDict):
            system("say I am sorry but there are not any purchases that have been stored!")
            return
        temp=self.ChoiceDict
        for index in temp.items():
            print str(index[0])+':'
            index_value = index[1].__dict__
            for index in index_value.items():
                print "{} = {}".format(*index)
            print

    def displaySec(self,name):
        if not any(self.ChoiceDict):
            system("say I am sorry but there are not any purchases that have been stored!")
            return
        for index in self.ChoiceDict[name].__dict__.items():
            print "{} = {}".format(index[0],index[1])
        return

    def doesExist(self, name):
        if not any(self.ChoiceDict):
            system("say I am sorry but there are not any purchases that have been stored!")
            return
        if name in self.ChoiceDict.keys():
            return False
        else:
            return True


