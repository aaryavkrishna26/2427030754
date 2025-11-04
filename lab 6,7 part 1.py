# Q1 create a python class called bank account which represent bank account havings attributres account number, name, balance.
# Q2 create a constructor with parameters account number, name, balance.
# Q3 create a deposit method which manages the deposit actions.
# Q4 create a withdrawl method which manages withdrawl actions.
# Q5 create a bank fees method to apply the bank fees with a  a percentage of 5% of the balance account.
# Q6 reate a display method to display account details.


class bankAccount() :
    def __init__(self,accno, name, balance):
        self.accno= accno
        self.name= name
        self.balance= balance

    def deposit(self, amount):
        self.balance += amount
        print("new balance= ", self.balance)

    def withdrawl(self, amount):
        self.balance -= amount
        print("new balance after withdrawl: ", self.balance)

    def bankfees(self):
        bank_fees= self.balance * 0.05
        print("bank fees= ", bank_fees)

    def show(self):
        print(f"my account no. is {self.accno} ")
        print(f"my name is {self.name} ")
        print(f"my balance is {self.balance} ")
bankaccount1= bankAccount(24436758, "aaryav", 100000)
bankaccount1.deposit(1000)
bankaccount1.withdrawl(2000)
bankaccount1.bankfees()
bankaccount1.show()

