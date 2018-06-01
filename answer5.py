class Expenditure:

    def __init__(self):
        self.salary=40000.0
        self.savings=2000.0
        self.category='m'
        self.totalexp=16000.0

    def AddExpenditure(self,category):
        if category=='f':
            self.category=category
            self.expenditure=26000.0
        elif category=='m':
            self.category=category
            self.expenditure=16000.0

    def CalcTotalExp(self):
        self.totalexp+=self.expenditure

    def CalcPerDayAndMonthlyExp(self):
        self.perDayExp=self.totalexp/365
        self.monthlyExp=self.totalexp/12


    def Display(self):
        print("Salary",self.salary,"\n")
        print("Savings",self.savings,"\n")
        print("Category",self.category,"\n")
        print("Expenditure",self.expenditure,"\n")
        print("Total Expenditure",self.totalexp,"\n")
        print("Per Month Expenditur",self.monthlyExp,"\n")
        print("Daily Expenditure",self.perDayExp,"\n")


ch='y'
while ch=='y':
    cat=input("Enter category: ")
    e1=Expenditure()
    e1.AddExpenditure(cat)
    e1.CalcTotalExp()
    e1.CalcPerDayAndMonthlyExp()
    e1.Display()
    ch=input("Do you want to enter more cases?? y\\n: ")