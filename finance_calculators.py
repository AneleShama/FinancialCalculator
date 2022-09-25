#references
#I used previous tasks to complete this Capstone Project
#L1T05 for casting variable so that if the diffrent capitalisation are same

#=============================================================================

#This program allows the user to access two different calculators: An Investment calculator and a home loan repayment calculator

import math

print("FINANCIAL CALCULATOR")

calculator_type = input("Choose either 'investment' or 'bond' from the menu below to proceed: \n \ninvestment \t- to calculate the amount of interest you'll earn on interest \nbond \t \t- to calculate the amount you'll have to pay on a home loan: \n")
calculator_type = calculator_type.lower() #cast input to lower cases

#Calculator for Investment Option
if calculator_type == "investment":
    principle_amount = float(input("Please Enter the amount you would want to deposit: \n"))
    interest_rate = float(input("What is the anticipated interest rate: \n"))
    num_years = float(input("How many years you planning to invest for: \n"))                   #number of years can also be thought as a float, if the user want to invest for 5 years and half, i.e 5.5

    interest_rate = interest_rate/100 #convert interest rate to percentage

    #Ask the user the type of interest they want to calculate
    interest = input("Which interest type do you want? Choose either 'simple' or 'compound': \n")
    interest = interest.lower()

    #Calculator for simple interest
    if interest == "simple":
        final_amount = round(principle_amount * ( 1 + interest_rate * num_years),2)
        interest_earned = round(final_amount - principle_amount,2)       #Interest earned from initail amount

        print("Here is what will happen to your Moola!")
        print(f"Deposited: \t \tR{principle_amount}")
        print(f"Interest Rate: \t \t{interest_rate}%")
        print(f"Number of years: \t{num_years}")
        print(" ")
        print(f"In {num_years} years time, at an interest rate of {interest_rate}% simple interest, you will have R{final_amount}")
        print(f"Your Moola is R{interest_earned} more")

    elif interest == "compound":
        final_amount = round(principle_amount * math.pow((1 + interest_rate),num_years),2)
        interest_earned = round(final_amount - principle_amount,2)       #Interest earned from initail amount

        print("Here is what will happen to your Moola!")
        print(f"Deposited: \t \tR{principle_amount}")
        print(f"Interest Rate: \t \t{interest_rate}%")
        print(f"Number of years: \t{num_years}")
        print(" ")
        print(f"In {num_years} years time, at an interest rate of {interest_rate}% compunded annually, you will have R{final_amount}")
        print(f"Your Moola is R{interest_earned} more")

    else:
        print(f"{interest} is an invalid selection")


#I used FNB resources
#https://www.fnb.co.za/calculators/homeloan/BondCalculator.html
#I used FNB Bond calculator to confirm if my code will give me the same result with thier calculators, and yes! it does


#Calculator for Bond Option
elif calculator_type == "bond":
    present_value = float(input("What is the present value of the house: \n"))
    interest_rate = float(input("What interest rate is the bank charging you: \n"))
    num_mounths = int(input("How many months are you planning to repay the bond: \n"))

    interest_rate = (interest_rate/100)/12 #interest is calculated mounthly

    repayment = round((interest_rate * present_value)/(1 - math.pow((1 + interest_rate),(-num_mounths))),2)

    tot_repayment = round(repayment * num_mounths,2) #Total amount paid at the end of the loan
    interest_charged = round(tot_repayment - present_value,2) #Amount of interest charged by the bank

    print("Here are the ins and out of your bond")
    print(f"Present value of the house: \t R{present_value}")
    print(f"Interest Charged: \t \t {interest_rate}%")
    print(f"Number of Months: \t \t {num_mounths}")
    print(" ")
    print(f"Each mounth you'll be paying R{repayment}")
    print(f"At the end of {num_mounths} months loan period you will have paid R{tot_repayment}, the interest the bank charged is R{interest_charged}")

#Invalid input
else:
    print(f"{calculator_type} is not a valid input, please choose either 'investment' or 'bond'. Restart the process")
