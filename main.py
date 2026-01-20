
# 1 - misol
balance = 1000
print("Sizning balansingiz:", balance)



# 2 - misol
balance = 1000

deposit = 500
balance = balance + deposit

withdraw = 300
balance = balance - withdraw

print("Yakuniy balans:", balance)



# 3 - misol
balance = 1000

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
    else:
        print("Balans yetarli emas")

deposit(500)
withdraw(300)

print("Balans:", balance)




# 4 - misol
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Xatolik: balans yetarli emas")

    def show_balance(self):
        print(self.owner, "balansi:", self.balance)


account = BankAccount("Ali", 1000)
account.deposit(500)
account.withdraw(200)
account.show_balance()




# 5 - misol
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print("O‘tkazma muvaffaqiyatli")
        else:
            print("Balans yetarli emas")


acc1 = BankAccount("Ali", 2000)
acc2 = BankAccount("Vali", 500)

acc1.transfer(700, acc2)

print("Ali balansi:", acc1.balance)
print("Vali balansi:", acc2.balance)



# 6 - misol
class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner
        self.balance = balance
        self.pin = pin

    def withdraw(self, amount, pin_input):
        if pin_input != self.pin:
            print("Noto‘g‘ri PIN!")
            return

        if amount <= self.balance:
            self.balance -= amount
            print("Pul yechildi")
        else:
            print("Balans yetarli emas")


account = BankAccount("Ali", 3000, 1234)
account.withdraw(500, 1234)
print("Balans:", account.balance)


























