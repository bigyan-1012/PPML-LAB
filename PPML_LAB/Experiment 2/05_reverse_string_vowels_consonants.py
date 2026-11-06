# Program 5: Reverse a string and count vowels and consonants
text = input("Enter a string: ")
print("Reversed string:", text[::-1])
vowels = sum(1 for ch in text if ch.isalpha() and ch.lower() in "aeiou")
consonants = sum(1 for ch in text if ch.isalpha() and ch.lower() not in "aeiou")
print("The vowels are:", vowels)
print("The consonants are:", consonants)
