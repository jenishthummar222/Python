l1 = ["python","java","php","flutter","android","AI","data science"]

l2 = list(filter(lambda st: len(st)>4,l1))

print(f"{l1}\n{l2}")