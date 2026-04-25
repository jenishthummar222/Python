product = {}   # blank Dictionary

menu = """
            MENU
    1:  Peoduct Manager
    2:  Customer
    3:  Exit
"""

status = True

while status:
    print(menu)

    role = int(input("Enter Your Role : "))

    if role == 1:
        print("\n******      Welcome To Manager Panal     ******\n")

        subDictionary = {}
        while True:
            print("""
                    MANAGE YOUR PRODUCT

                1: Add New Product
                2: View Product
                3: Remove Product
                4: Exit
            """)
            manager_choice = int(input("Enter Your Choice :- "))

            if manager_choice == 1:
                print("\n*********      Add New Product     *********\n")

                product_name = input("Enter Your Product Name :- ")
                price = int(input("Enter Your Price :- "))
                discout = int(input("Enter Your Discout :- "))
                food_type = input("Enter Food Type (jain / regular / spicy / non-spicy) : ")


            # add containt in subdict

                subDictionary["price"] = price                
                subDictionary["discout"] = discout
                subDictionary["food_type"] = food_type

            # add sub-dict in product

                product[product_name] = subDictionary

                print("\n*********      Product Added Successfully...     *********\n")


            elif manager_choice == 2:
                print("\n*********      View Product     *********\n") 
                for k,v in product.items():
                    print(f"{k} |   price : {product[k]["price"]} |   Discount : {product[k]["discout"]} |   Food Type : {product[k]["food_type"]}")
                    print("------------------------------------------------------------------------------------------------")

            elif manager_choice == 3:
                del_product = input("Enter Your Remove Product Name :- ")

                del product[del_product]

                if del_product not in product:
                    print("Product Deleted Successfully")
                else:
                    print("Product Is not deleted...")


            else:
                break


    elif role == 2:
        pass
    else:
        status = False
