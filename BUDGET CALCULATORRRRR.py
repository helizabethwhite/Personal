import time
## money earned
## money saved
## money for bills
## money for spending

earned = 0
saved = 0
bills = 0
spending = 0
bill_amt = 0
twenty_perc = 0
newly_bills = 0
newly_spending = 0

print(" "*15 + "*"*47)
print(" "*15 + "*WELCOME TO HANNAH'S AMAZING BUDGET CALCULATOR*")
print(" "*15 + "*"*47)
print()
true = input("Is it the beginning of a new month? (y/n): ")
bill_amt = input("Enter bill amount: ")
bill_amt = float(bill_amt)

print("")
if true == 'y':
    f = open("bills.txt", "w")
else:
    f = open("bills.txt","r")

    count = 0
    for line in f:
        line.strip("\n")
        line = float(line)
        if count == 0:
            earned = line
            count += 1
        elif count == 1:
            saved = line
            count += 1
        elif count == 2:
            bills = line
            count += 1
        elif count == 3:
            spending = line
            count += 1
    f.close()
    f = open("bills.txt", "w")


print("CURRENT ASSETS FOR THIS MONTH are as follows: ")
print("-"*40)
print("Your money earned: ", earned)
print("Your money saved: ", saved)
print("Your money put towards bills: ", bills)
print("Your money for spending: ", spending)

print()
paycheck = input("Enter the amount of your latest paycheck: ")
paycheck = float(paycheck)
earned += paycheck


twenty_perc = paycheck * .20
saved += twenty_perc

##figure = .45
##while(bills < bill_amt):
##    while(bills + (paycheck*figure)) >= bill_amt:
       

if bills >= bill_amt:
    pass
elif (bills + (paycheck*.45)) >= bill_amt:
    if (bills + (paycheck*.425)) >= bill_amt:
        if (bills + (paycheck*.40)) >= bill_amt:
            if (bills + (paycheck*.35)) >= bill_amt:
                if (bills + (paycheck*.325)) >= bill_amt:
                    if (bills + (paycheck*.30)) >= bill_amt:     
                        if (bills + (paycheck*.25)) >= bill_amt:           
                            if (bills + (paycheck*.20)) >= bill_amt:  
                                if (bills + (paycheck*.15)) >= bill_amt:
                                    if (bills + (paycheck*.10)) >= bill_amt:
                                        if (bills + (paycheck*.05)) >= bill_amt:
                                            if (bills + (paycheck*.025)) >= bill_amt:
                                                newly_bills = (paycheck*.025)
                                                bills += newly_bills
                                        else:
                                            newly_bills = (paycheck*.05)
                                            bills += newly_bills
                                    else:
                                        newly_bills = (paycheck*.10)
                                        bills += newly_bills
                                else:
                                    newly_bills = (paycheck*.15)
                                    bills += newly_bills
                            else:
                                newly_bills = (paycheck*.20)
                                bills += newly_bills
                        else:
                            newly_bills = (paycheck*.25)
                            bills += newly_bills
                    else:
                        newly_bills = (paycheck*.30)
                        bills += newly_bills
                else:
                    newly_bills = (paycheck*.325)
                    bills += newly_bills
            else:
                newly_bills += (paycheck*.35)
                bills += newly_bills
        else:
            newly_bills += (paycheck*.40)
            bills += newly_bills
    else:
            newly_bills += (paycheck*.425)
            bills += newly_bills
else:
      newly_bills = (paycheck*.45)
      bills += newly_bills

spending = (earned - saved - bills)
newly_spending = (paycheck-twenty_perc-newly_bills)

print("")
print("UPDATED MONTHLY ASSETS are as follows: ")
print("-"*40)
print("Your new money earned: ", paycheck)
print("Your new money saved (20%): ", round(twenty_perc,2))
print("Your new money put towards bills (if goal not already reached): ", round(newly_bills,2))
print("Your new money for spending: ", round(newly_spending,2))
print("-"*40)
print("Your total money earned: ", earned)
print("Your total money saved: ", round(saved,2))
print("Your total money put towards bills: ", round(bills,2))
print("Your total money for spending: ", round(spending,2))

print(round(float(earned),2), file=f)
print(round(float(saved),2), file=f)
print(round(float(bills),2), file=f)
print(round(float(spending),2), file=f)
f.close()
time.sleep(60)


