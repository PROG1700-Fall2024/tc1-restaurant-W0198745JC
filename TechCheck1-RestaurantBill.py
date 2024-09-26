#PROG 1700 – Tech Check #1
#Variables, Operators, Input/Output & Casting

# Restaurant Bill 
# You will create a console-based Python program that will calculate the amount of the tip, the tax, and the 
# total amount of a restaurant bill. The program will prompt the user to input the original amount of the bill. 
# The program will then output the amount of the tax (15% of the original amount) and a tip (20% of the original amount). 
# Finally, the program will output the new total of the bill.


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

#input variable for bill
    bill=input("Please enter your original bill amount: ")
#taxes 15/100
    taxes=15/100
#taxes*bill
    billTax=taxes*int(bill)
#Tip 20/100
    tip=20/100
#Tip*bill
    billTip=tip*int(bill)
#total for bill
    totalBill=int(bill)+billTax+billTip
#print all bill , taxes , tip , and total
    print("Your original bill amount is: ${0:.2f}".format(float(bill))) 
    print("Your Tax is: ${0:.2f}".format(billTax))
    print("Your tip is: ${0:.2f}".format(billTip))
    print("Your total is: ${0:.2f}".format(totalBill))






    # YOUR CODE ENDS HERE

main()