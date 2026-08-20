# PYTHON PROGRAM TO COUNT THE NUMBER OF VOWELS PRESENT IN A STRING USING SETS ?

text = input("Enter a string: ")

vowels = set("aeiouAEIOU")
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)