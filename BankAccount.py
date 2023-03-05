import os,sys
class Account:
    def __init__(self, name,accountNo, accountType,balance ):
        self.name=name
        self.accountNo=accountNo
        self.accountType=accountType
        self.balance=balance
    def displayBalance(self):
        return self.balance
    def depositeMoney(self, deposite):
        self.balance+=deposite
        print(f"\n\nYou have deopsited {deposite}$, your balance is currently {self.balance}$\n\n")
    def withdrawMoney(self, withdraw):
        if(self.balance<withdraw):
            print( "\n\nyou dont have this amount of money to withdraw\n\n")
        else:
            self.balance-=withdraw
            print(f"\n\nYou have withdrawn {withdraw}$, your balance is currently {self.balance}$\n\n") 
    

class sav_acct(Account):
    annualRate=0.01 ##interestrate
    def __init__(self, name, accountNo, accountType, balance):
        super().__init__(name, accountNo, accountType, balance)
    def interest(self,NoOfYears):
        interestEaarned=int(self.balance*(((sav_acct.annualRate)+1)**NoOfYears)-self.balance)
        self.balance=int(self.balance*(((sav_acct.annualRate)+1)**NoOfYears))
        print(f"\n\nYour interestEaned is{interestEaarned}$ , your balance is currently {self.balance}$\n\n")

class cur_acct(Account):
    minumumBalance=1000
    serviceCharge=0.1
    def __init__(self, name, accountNo, accountType, balance):
        super().__init__(name, accountNo, accountType, balance)
    def balanceCheck(self):
        if self.balance<cur_acct.minumumBalance:
            return True
        return False
    def imposePenalty(self):
        if self.balanceCheck():
            penalty=int(self.balance*cur_acct.serviceCharge)
            self.balance-=int(self.balance*cur_acct.serviceCharge)##update balance
            print(f"\n\nYour account is less than minimum balance, and the pelenty {penalty}$ was imposed to your balance, your balance is currently {self.balance}$\n\n ")
        else:
            print("\n\nYour account is more than minimum balance, No penalty to impose\n\n")
def main():
            Name=input("Enter your name: ")
            AccountNo=input("Enter your Account No: ")
            Type=input("Current account or Saving Account(C, S): ")
            balance=int(input("How much do you want to deopsit as a start: "))
            if(Type.upper()=='C'):
                accountholder=cur_acct(Name,AccountNo, Type, balance)
                print(f"you have created an account, card number:{accountholder.accountNo} for {accountholder.name} is a current accoount with balance: {accountholder.balance}$")
                def updateBalance(): ##function to update balance in file with each operation
                    InFile=open(os.path.join(sys.path[0], 'CAH.txt'), 'r') ##sys.path[0] for files in the same folder
                    data = InFile.readlines(); InFile.close()
                    for line in data:
                        if (line.startswith("card number:"+AccountNo)):
                            l=data.index(line)
                            data[l]=f"card number:{accountholder.accountNo} for {accountholder.name} is a current accoount with balance: {accountholder.balance}$ \n"
                            f=open(os.path.join(sys.path[0], 'CAH.txt'), 'w')
                            f.writelines(data)
                            f.close()
                InFile=open(os.path.join(sys.path[0], 'CAH.txt'), 'a')
                InFile.write(f"\ncard number:{AccountNo} for {Name} is a current accoount with balance: {balance}$ \n")
                InFile.close()
                operation=''
                while operation.upper()!='E':
                    operation= input(" \nChoose one of the following operations to do: \nA.Accept deposit from a customer and update the balance. \nB.Display the balance. \nC.Permit withdrawal and update the balance.\nD.Check for the minimum balance, impose a penalty, necessary, and update the balance.\nE. Done! \n")
                    if(operation.upper()=='A'):
                        deposite=int(input("Enter money to deposite: "))
                        accountholder.depositeMoney(deposite)
                        updateBalance()
                    elif(operation.upper()=='B'):
                        InFile=open(os.path.join(sys.path[0], 'CAH.txt'), 'r')
                        for line in InFile:
                                if (line.startswith("card number:"+AccountNo)):
                                    print("\n\n", line, "\n\n")
                        InFile.close()
                    elif(operation.upper()=='C'):
                        withdraw=int(input("Enter money to withdraw: "))
                        accountholder.withdrawMoney(withdraw)
                        updateBalance()
                    elif(operation.upper()=='D'):
                        accountholder.imposePenalty()
                        updateBalance()
                    elif(operation.upper()=='E'):
                        break
                    else:
                        print("You have to choose one of the operations")
            elif(Type.upper()=='S'):
                accountholder=sav_acct(Name,AccountNo, Type, balance)
                print(f"you have created an account, card number:{accountholder.accountNo} for {accountholder.name} is a saving accoount with balance: {accountholder.balance}$")
                def updateBalance():
                    InFile=open(os.path.join(sys.path[0], 'SAH.txt'), 'r')
                    data = InFile.readlines(); InFile.close()
                    for line in data:
                        if (line.startswith("card number:"+AccountNo)):
                            l=data.index(line)
                            data[l]=f"card number:{accountholder.accountNo} for {accountholder.name} is a saving accoount with balance: {accountholder.balance}$ \n"
                            f=open(os.path.join(sys.path[0], 'SAH.txt'), 'w')
                            f.writelines(data)
                            f.close()
                InFile=open(os.path.join(sys.path[0], 'SAH.txt'), 'a')
                InFile.write(f"\ncard number:{AccountNo} for {Name} is a saving accoount with balance: {balance}$ ")
                InFile.close()
                operation=""
                while operation.upper()!='E':
                    operation= input("\n Choose one of the following operations to do: \nA.Accept deposit from a customer and update the balance. \nB.Display the balance. \nC.Permit withdrawal and update the balance.\nD.Compute and deposit interest.\nE. Done! \n")
                    if(operation.upper()=='A'):
                        deposite=int(input("Enter money to deposite: "))
                        accountholder.depositeMoney(deposite)
                        updateBalance()
                    elif(operation.upper()=='B'):
                        InFile=open(os.path.join(sys.path[0], 'SAH.txt'), 'r')
                        for line in InFile:
                                if (line.startswith("card number:"+AccountNo)):
                                    print("\n\n",line,"\n\n")
                        InFile.close()
                    elif(operation.upper()=='C'):
                        withdraw=int(input("Enter money to withdraw: "))
                        accountholder.withdrawMoney(withdraw)
                        updateBalance()
                    elif(operation.upper()=='D'):
                        noofyears=int(input("Enter the no of years your money exesits? "))
                        accountholder.interest(noofyears)
                        updateBalance()
                    elif(operation.upper()=='E'):
                        break
                    else:
                        print("You have to choose one of the operations")
main()