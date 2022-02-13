import withdrawal_Function

class Budget:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount    

    def deposit(self, amount):
        self.balance += amount

# setting the balance for each category
food = Budget(50)
clothing = Budget(20)
entertainment = Budget(70)
pets = Budget(12)

userInput = ''

def menu():
    userInput = input("Choose an item: \n (F)ood, \n (C)lothing, \n (E)ntertainment, \n (P)ets,\n (B)alance, \n (Q)uit \n" )
    while userInput != 'q':
        if userInput == 'f':
            while userInput != 'r':
                print("Current balance:", food.balance)
                userInput = input("Choose an item: \n (D)eposit, \n (W)ithdraw, \n (T)ransfer, \n (R)eturn \n")
                if userInput == 'd':
                    userInput = float(input("How much would you like to deposit?: "))
                    food.deposit(userInput)
                elif userInput == 'w':
                    userInput = float(input("How much would you like to withdraw?: "))
                    food.withdraw(userInput)
                elif userInput == 't':
                    userInput = float(input("How much would you like to transfer?: "))
                    transferAmount = userInput
                    food.balance -= transferAmount
                    userInput = input("Where would you like to transfer?: \n (C)lothing, \n (E)ntertainment, \n (P)ets, \n (Q)uit \n")
                    if userInput == 'c':
                        clothing.balance += transferAmount
                    elif userInput == 'e':
                        entertainment.balance += transferAmount
                    elif userInput == 'p':
                        pets.balance += transferAmount 
            else:
                menu()
        elif userInput == 'c':
            while userInput != 'r':
                print("Current balance: ", clothing.balance)
                userInput = input("Choose an item: \n (D)eposit, \n (W)ithdraw, \n (T)ransfer, \n (R)eturn \n")
                if userInput == 'd':
                    userInput = float(input("How much would you like to deposit?: "))
                    clothing.deposit(userInput)
                elif userInput == 'w':
                    userInput = float(input("How much would you like to withdraw?: "))
                    clothing.withdraw(userInput)
                elif userInput == 't':
                    userInput = float(input("How much would you like to deposit?: "))
                    clothing.deposit(userInput)
                elif userInput == 't':
                    userInput = float(input("How much would you like to transfer?: "))
                    transferAmount = userInput
                    clothing.balance -= transferAmount
                    userInput = input("Where would you like to transfer?: \n (F)ood, \n (E)ntertainment, \n (P)ets, \n (Q)uit \n")
                    if userInput == 'f':
                        food.balance += transferAmount
                    elif userInput == 'e':
                        entertainment.balance += transferAmount
                    elif userInput == 'p':
                        pets.balance += transferAmount 
            else:
                menu()
        elif userInput == 'e':
            while userInput != 'r':
                print("Current balance: ", entertainment.balance)
                userInput = input("Choose an item: \n (D)eposit, \n (W)ithdraw, \n (T)ransfer, \n (R)eturn \n")
                if userInput == 'd':
                    userInput = float(input("How much would you like to deposit?: "))
                    entertainment.deposit(userInput)
                elif userInput == 'w':
                    userInput = float(input("How much would you like to withdraw?: "))
                    entertainment.withdraw(userInput)
                elif userInput == 't':
                    userInput = float(input("How much would you like to transfer?: "))
                    transferAmount = userInput
                    entertainment.balance -= transferAmount
                    userInput = input("Where would you like to transfer?: \n (F)ood, \n (C)lothing, \n (P)ets, \n (Q)uit \n")
                    if userInput == 'f':
                        food.balance += transferAmount
                    elif userInput == 'c':
                        clothing.balance += transferAmount
                    elif userInput == 'p':
                        pets.balance += transferAmount 
            else:
                menu()
        elif userInput == 'p':
            while userInput != 'r':
                print("Current balance: ", pets.balance)
                userInput = input("Choose an item: \n (D)eposit, \n (W)ithdraw, \n (T)ransfer, \n (R)eturn \n")
                if userInput == 'd':
                    userInput = float(input("How much would you like to deposit?: "))
                    pets.deposit(userInput)
                elif userInput == 'w':
                    userInput = float(input("How much would you like to withdraw?: "))
                    pets.withdraw(userInput)
                elif userInput == 't':
                    userInput = float(input("How much would you like to transfer?: "))
                    transferAmount = userInput
                    pets.balance -= transferAmount
                    userInput = input("Where would you like to transfer?: \n (F)ood, \n (C)lothing, \n (E)ntertainment,\n (Q)uit \n")
                    if userInput == 'f':
                        food.balance += transferAmount
                    elif userInput == 'c':
                        clothing.balance += transferAmount
                    elif userInput == 'e':
                        entertainment.balance += transferAmount 
                else:
                    menu()
        elif userInput == 'b':
            # for i in (food.balance, clothing.balance, entertainment.balance, pets.balance):
            #     print([i])
            print("Food balance: ", food.balance)
            print("Clothing balance: ", clothing.balance)
            print("Entertainment balance :", entertainment.balance)
            print("Pet balance: ", pets.balance)
            menu()
    quit()

menu()
print("end of program")