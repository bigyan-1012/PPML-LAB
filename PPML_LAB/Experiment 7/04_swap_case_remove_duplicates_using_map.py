# Program 4: Convert characters to opposite case using map() and remove duplicates
characters = input("Enter a sequence of characters: ")
def swap_case(character):
    if character.isupper():
        return character.lower()
    if character.islower():
        return character.upper()
    return character
changed = list(map(swap_case, characters))
unique_characters = list(dict.fromkeys(changed))
print("Updated sequence without duplicates:", "".join(unique_characters))
