import re

# Open and read the text file
with open("sample.txt", "r") as file:
    text = file.read()

# Regular expression pattern for email addresses
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Find all email addresses
emails = re.findall(pattern, text)

# Display the email addresses
print("Email addresses found:")
for email in emails:
    print(email)