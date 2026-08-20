# PYTHON PROGRAM TO CHECK COMMON LETTERS IN TWO INPUT STRING ?

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

common = set(str1) & set(str2)

print("Common letters:", common)