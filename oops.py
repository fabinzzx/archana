class bankaccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.__balance=balance
        
    def deposit(self,amount):
         if amount>0:
            self.__balance+=amount
            print(f"deposited:{amount},new balance:{self.__balance}")
         else:
            print("deposit amount must be positive.")
    def withdraw(self,amount):
        if 0 < amount<=self.__balance:
            self.__balance-=amount
            print(f"withdraw:{amount},remaining balance:{self.__balance}")
        else:
            print("invalid withdrawal amount.")

    def get_balance(self):
            return self.__balance
acc=bankaccount("joseph",1000)
acc.deposit(500)
acc.withdraw(300)
print("final balance:",acc.get_balance())

                

