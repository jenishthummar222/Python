"""
Project Title
Clothing Store Billing System 

"""

name = input("Enter Your Name :- ")
item = input("Enter your Item (Shirt/ Jeans/ Jacket) :- ")
price = int(input("Enter Yor price :- "))
quantity = int(input("Enter Quantity :- ")) 

totalAmount = price * quantity

disc_amount=0

if totalAmount>=500 and totalAmount<=999:
    disc_amount = totalAmount - (totalAmount * 10 / 100)
elif totalAmount>=1000 and totalAmount<=1999:
    disc_amount = totalAmount - (totalAmount * 20 / 100)
elif totalAmount>=2000 :
    disc_amount = totalAmount - (totalAmount * 30 / 100)

extra_disc =0

if item =="Shirt":
    extra_disc = disc_amount - (disc_amount * 5 /100)
elif item =="Jeans":
    extra_disc = disc_amount - (disc_amount * 8 /100)
elif item =="Jacket":
    extra_disc = disc_amount - (disc_amount * 12 /100)

gst =0

if extra_disc < 1000 :
    gst = (extra_disc*5/100)
else :
    gst = (extra_disc*12/100)

print("---- Final Bill ----")
print(f"Customer Name :- {name}")
print(f"Item Name :- {item}")
print(f"Price :- {price}")
print(f"Quantity :- {quantity}")
print(f"Total Amount :- {totalAmount}")
print(f"Discount Applied :- {disc_amount}")
print(f"Extra Discount :- {extra_disc}")
print(f"GST Amount  : {gst}")
print(f"Final Payable Amount :- {gst+extra_disc}")


