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
                    userInput = float(input("How much would you like to deposit?: "))
                    food.deposit(userInput)
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
                    userInput = float(input("How much would you like to deposit?: "))
                    entertainment.deposit(userInput)
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
                    userInput = float(input("How much would you like to deposit?: "))
                    pets.deposit(userInput)
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

# def food_menu():

#     print(food.balance)

#     userInput = input("(W)ithdraw balance \n (D)eposit balance \n (T)ransfer balance \n (M)enu \n")
#     if userInput == 'w':
#         userAmount = input("Enter amount to withdraw: ")
#         userAmount = float(userAmount)
# #        strvar.withdraw(userAmount)
#         return userAmount
#     elif userInput == 'd':
#         pass
#     elif userInput == 't':
#         pass
#     else:
#         menu()    







# # withdrawal
# while True:
#     menuInput = input("Enter\n (F)ood, \n (C)lothing, \n (E)ntertainment, \n (P)ets,\n (Q)uit \n" )
#     if menuInput == 'f':
#         print("Current food balance: ", food.balance)
#         withdrawal(food)
#         print("Remaining food balance:", food.balance)
#         continue
#     elif menuInput == 'c':
#         print("Current clothing balance: ", clothing.balance)
#         withdrawal(clothing)
#         print("Remaining clothing balance:", clothing.balance)
#         continue
#     elif menuInput == 'e':
#         print("Current entertainment balance: ", entertainment.balance)
#         withdrawal(entertainment)
#         print("Remaining entertainment balance:", entertainment.balance)
#         continue
#     elif menuInput == 'p':
#         print("Current pet balance: ", pets.balance)
#         withdrawal(pets)
#         print("Remaining pet balance:", pets.balance)
#         continue
#     elif menuInput == "q":
#         break


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