# Program 5: Print words having even length
text = input("Enter a string: ")
print("Even length words:")
for word in text.split():
    if len(word) % 2 == 0:
        print(word)
