# ATM (Automated Teller Machine ) 
                   
print("\nHello welcome to my ATM machine\n") 
print("Please enter your card \n") 
Password=int(input("Please enter your 5 digit code : "))
Balance=10000
Pin=12345
if Pin==Password:
    print("Welcome to my ATM machine\n")
    language=input("Please choose your language :\n\n1.Hindi\n2.English\n\nSelect your language :-  ")
    if language=="1":
        print("Hindi is not avalable please contnue in English :-  ")
    elif language=="2":
        print("Thanks for choose english language ok lets go")
    transaction=input("\nWhat do you want :\n\n1.Widraw\n2.Balance Enqueri\n3.Cash Deposit\n\nChoose any option :- ")
    if transaction=="1":
       Widraw=int(input("Please enter widraw amount : "))
       if Widraw<=Balance:
           cash=Balance-Widraw
           print(Widraw, "is debited from your account:")
           print(cash, "is your total balance... Thank You ")
       else:
           print("You entered invalid amount ")
    elif transaction=="2":
        print(Balance," is your currect balance....Thank You")
    elif transaction=="3":
        Cashdeposit=int(input("Please enter Cash Deposit amount : "))
        Cash=Balance+Cashdeposit
        print(Cash,"is your total balance....Thank You")

else:
    print("Soryy you enter wrong pin please try again")