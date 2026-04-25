# with parameter and return type

def isPalindrom(str1):
    return "is Palindrom" if str1 == str1[::-1] else "is not Palindrom"

print(isPalindrom("mom"))
print(isPalindrom("ram"))