"""
    Create a Python program that allows a shopkeeper to generate a bill for grocery items using input, 
    variables, for loop, and conditional statements.

    Project Description (Advanced Grocery Billing System)

"""

c_name = input("Enter Your Name :- ")
c_member = input("You are member ? (yes/no) :- ")

number_of_item = int(input("Enter Number of Items :- "))

quantity,price,item_total,total_bill,discount = 0,0,0,0,0

for i in range(1,number_of_item+1):

    p_name = input("Enter item Name :- ")
    quantity = int(input("Enter Quantity :- "))
    price = int(input("Enter Item Price :-"))

    item_total = price * quantity 

    if quantity >= 5:
       #item_total-=(item_total*0.05)
        discount += (item_total*0.05)

    total_bill += item_total

if total_bill >= 2000:
    #total_bill -= (total_bill*0.15)
    discount += (total_bill*0.15)
elif  total_bill >=1000:
   # total_bill -= (total_bill*0.10)
    discount += (total_bill*0.10)
elif total_bill >=500:
    #total_bill -= (total_bill*0.05)
    discount += (total_bill*0.05)
else:
    print("No Discount")


if c_member =="yes":
    #total_bill -= (total_bill*0.05)
    discount += (total_bill*0.05)

GST = total_bill * 0.18 

print("\n---- final bill ----")
print("Customer name : ",c_name)
print("Total Amount : ",total_bill)
print("Discount : ",discount)
print("GST : ",GST)
print("Final payable amount : ",(total_bill-discount+GST))



