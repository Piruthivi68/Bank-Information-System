#Initialize variables
publics=[]
count=4

#Print main details
while(count>3):
    print("         ABC BANK")
    print("        Main Menu")
    print("1. Add a New Customer")
    print("2. view details of a customer")
    print("3. View details of all customers")
    print("4. Deposit money to an account")
    print("5. Withdraw money from an account")
    print("6. Update a customer details")
    print("7. EXIT")
    choice=input("                                 Enter your choice: ")

#Get input from the user
    if choice=="1":
        print("         ABC BANK")
        print("    Add a new customer")
        if len(publics)<5:
            public_account_number=input("Enter Customer's Account Number: ")
            public_nic_number=str(input("Enter Customer's NIC Number: "))
            public_first_name=str(input("Enter Customer's First Name: "))
            public_last_name=str(input("Enter Customer's Last Name: "))
            date_of_birth=input("Enter Customer's Date Of Birth: ")
            permanent_address=str(input("Enter the Customer's Permanent Address: "))
            telephone_number=str(input("Enter the Customer's Telephone Number: "))
            balance=0.0
            if input("DO you want to save the Account details ? : ")==("yes"):
                publics.append([public_account_number, public_nic_number, public_first_name, public_last_name, date_of_birth, permanent_address, telephone_number, balance])
                print("Account details saved successfully.")
            else:
                print("Account details cannot be saved.")
        else:
            print("Maximum numbers of customers reached cannot add more!!")

#choice 2
    elif choice=="2":
        print("          ABC BANK")
        print("    View details of a customer")
        public_account_number=input("Enter Account Number: ")
        for  public in publics:
            if public[0] == public_account_number:
                print("Customer Account Number: ",public[0])
                print("Customer NIC Number: ",public[1])
                print("Customer Telephone Number: ",public[6])
                print("Customer First Name: ",public[2])
                print("Customer Last Name: ",public[3])
                print("Bank Balance: ",public[7])
                if input("Do you want to view another account details ? : ")==("yes"):
                    print()
                else:
                    print("Thank you For Using Our Service")
                    break
                break
        else:
            print("Error: Cannot Find The Account!!")

#choice 3
    elif choice=="3":
        print("            ABC BANK")
        print("  View details of all customers")
        for public in publics:
             print("Customer NIC Number: "
                   ,public[1])
             print("Customer Account Number: "
                   ,public[0])
             print("Customer First Name: "
                   ,public[2])
             print("Customer Last Name: "
                   ,public[3])
             print("Bank Balance: "
                   ,public[7])

        if input("Do you want to update the account details ? : ")==("yes"):
            print("Thank you For Using Our Services")
        else:
            print("Thank you For Using Our Servics")
   
#choice 4
    elif choice=="4":
        print("            ABC BANK")
        print("         Deposit Money")
        public_account_number=input("Enter Account Number: ")
        for public in publics:
            if public[0] == public_account_number:
                cash=float(input("Enter the amount to deposit: "))
                if input("Do you want to save ? : ")==("yes"):
                    public[7]+=cash
                    print("Deposit successful. New balance: ",public[7])
                else:
                    print("Deposit Failed.")
                break
        else:
            print("Error: Cannot Find The Account!!")


#choice 5
    elif choice=="5":
        print("             ABC BANK")
        print("          Withdraw Money")
        public_account_number=input("Enter Account Number: ")
        for public in publics:
            if public[0] == public_account_number:
                cash=float(input("Enter the amount to withdraw: "))
                if public[7]>=cash:
                    if input("Do you want to save ? : ")==("yes"):
                        public[7]-=cash
                        print("Withdraw successful. New balance: ",public[7])
                    else:
                        print("Insufficient Balance In The Account.")
                break
            else:
                print("Error: Cannot Find The Account!!")

#choice 6
    elif choice=="6":
        print("              ABC BANK")
        print("     Update Customer Details")
        public_account_number=input("Enter Account Number: ")
        for public in publics:
            if public[0]==public_account_number:
                print("customer found!!!")
                confirm_update=input("Confirm Update:- Do you want to update your customer details: ")
                if(confirm_update=="yes"):
                    public[1]=input("Enter Customer's new NIC Number: ")
                    public[2]=input("Enter Customer's new First Name: ")
                    public[3]=input("Enter Customer's new Last Name: ")
                    public[4]=input("Enter Customer's new Date of Birth: ")
                    public[5]=input("Enter Customer's new Address: ")
                    public[6]=input("Enter Customer's new Telephone Number: ")
                    public[7]=float(input("Enter The New Account Balance: "))
                    print("Customer details updated successfully.")
                    
                else:
                    print("Cannot updated customer details.")
            else:
                print("Error: Cannot Find The Account!!")

#choice 7
    elif choice=="7":
        print("               ABC BANK")
        print("EXIT, Thank you for using our service")
        

    else:
        print("Invalid Choice! Please Try Again...")

    

        
