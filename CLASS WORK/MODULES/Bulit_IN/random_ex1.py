from random import random

otp = random.randint(1111,9999)

print(f"OTP :: {otp}")

subject_list = ["python","java","php","AI"]
print(f"subject :- {subject_list}")
print(random.choice(subject_list))

print(random.random())