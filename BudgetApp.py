# create class called budget and enter the attributes: self, food, clothing, entertainment
# create a way for these objects to allow depositing and withdrawing funds (method) inside class

class Budget:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount    

    def deposit(self, amount):
        self.balance += amount

    # #if userInput == 'w' or 'W':
    #     print("Which category would you like to withdraw from?: \n '\Food', \n 'Clothing' \n 'Entertainment', \n 'Pets' \n")
    #     if userInput == "food":
    #         print("Food balance:", food.balance)
    #         userAmount = input("Enter amount to withdraw: ")
    #         userAmount = int(userAmount)    


# menu()

# setting the balance for each category
food = Budget(50)
clothing = Budget(20)
entertainment = Budget(70)
pets = Budget(12)

userInput = ''

def withdrawal(strvar):
    userAmount = input("Enter amount to withdraw: ")
    userAmount = float(userAmount)
    strvar.withdraw(userAmount)
    return userAmount


while True:
    menuInput = input("Enter (F)ood, \n (C)lothing, \n (E)ntertainment, \n (P)ets,\n (Q)uit \n" )
    if menuInput == 'f':
        print("Current food balance: ", food.balance)
        withdrawal(food)
        print("Remaining food balance:", food.balance)
        continue
    elif menuInput == 'c':
        print("Current clothing balance: ", clothing.balance)
        withdrawal(clothing)
        print("Remaining clothing balance:", clothing.balance)
        continue
    elif menuInput == 'e':
        print("Current entertainment balance: ", entertainment.balance)
        withdrawal(entertainment)
        print("Remaining entertainment balance:", entertainment.balance)
        continue
    elif menuInput == 'p':
        print("Current pet balance: ", pets.balance)
        withdrawal(pets)
        print("Remaining pet balance:", pets.balance)
        continue
    elif menuInput == "q":
        break


    pass

print("Outside while loop")

# # this goes into the withdraw method within the class and takes away the amount specified
# food.withdraw(userAmount)
# clothing.withdraw(userAmount)
# entertainment.withdraw(userAmount)
# pets.withdraw(userAmount)

# print("Food balance:", food.balance)
# print("Clothing balance:", clothing.balance)
# print("Entertainment balance:", entertainment.balance)
# print("Pet balance", pets.balance)

# # this goes into the deposit method within the class and adds the amount specified
# food.deposit(20)
# clothing.deposit(10)
# entertainment.deposit(100)
# pets.deposit(8)

# print("Food balance:", food.balance)
# print("Clothing balance:", clothing.balance)
# print("Entertainment balance:", entertainment.balance)
# print("Pet balance", pets.balance)