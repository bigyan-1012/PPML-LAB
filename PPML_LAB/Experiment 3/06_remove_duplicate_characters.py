# Program 6: Remove duplicate characters from a string
text = input("Enter a string: ")
result = ""

for character in text:
    if character not in result:
        result += character

print("String after removing duplicates:", result)
