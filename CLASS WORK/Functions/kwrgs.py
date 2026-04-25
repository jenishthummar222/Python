# key with arguments :- kwargs

def student (**kwrgs):
    for k,v in kwrgs.items():
        print(f"{k} = {v}")

student(name="jenihs",subject="python",score = 90)