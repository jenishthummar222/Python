l1=[60,50,90,70,82,82]

# with list comprihension.

l2 = ["A" if num<=100 and num>90 else
      "B" if num<=90 and num>80 else
      "C" if num<=80 and num>70 else
      "D" if num<=70 and num>=60 else
      "Fail" for num in l1]

print(l1)
print(l2)


    