menu = """

                MENU
    ---------------------------
        1: add new Element
        2: remove Element
        3: Remove Last Element
        4: Remove Specific Index Element
        5: Exit

        """


status = True
list =[]

while status:
    print(menu)
    print()
    choice = int(input("Enter Your Choice :- "))

    match choice:
        case 1: 
            elemt = int(input("Enter Your Total Element Number :- "))

            for i in range(elemt):
                list.append(input(f"Enter your {i+1} Element :- "))

            print("All elements are added..")

        case 2:
            print("Your List ::-")
            for i in list:
                print(i,end=" ")

            elemt = input("\nWhich Element you want to remove :- ")            
            if elemt in list:
                list.remove(elemt)
                print(f"\n{elemt} is Removed..")

        case 3:
            print("Your List ::-")
            for i in list:
                print(i,end=" ")            
            print(f"\n{list.pop()} Element is Removed..")
        
        case 4:
            print("Your List ::-")
            for i in list:
                print(i,end=" ")

            elemt = int(input("\nWhich Element you want to remove Enter Index:- "))

            if list[elemt-1] in list:                
                print(f"\n{list[elemt-1]} is Removed..")
                list.pop(elemt-1)
            else:
                print("Index is Out Of Range..")
        
        case _:
            status=False
            print("Byyy..")