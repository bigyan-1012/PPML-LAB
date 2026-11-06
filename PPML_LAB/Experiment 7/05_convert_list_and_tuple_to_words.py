# Program 5: Convert a list and tuple of integers into lists of number words using map()
words = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
         5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
convert = lambda number: words.get(number, "unknown")

numbers_list = [int(x) for x in input("Enter list integers separated by spaces: ").split()]
list_words = list(map(convert, numbers_list))
print("Converted list:", list_words)

numbers_tuple = tuple(int(x) for x in input("Enter tuple integers separated by spaces: ").split())
tuple_words = list(map(convert, numbers_tuple))
print("Converted tuple as list of words:", tuple_words)
