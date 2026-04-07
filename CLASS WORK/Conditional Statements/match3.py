number = int(input("Enter a Number :- "))

match number:
    case number if number > 0:
        print("Number is Positive.")
    case numner if number < 0:
        print("Number is Nagative.")
    case _:
        print("number is Zero")