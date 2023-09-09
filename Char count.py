input_string = input("Enter a string: ")
char_to_count = input("Enter the character to count: ")
count = 0
for char in input_string:
    if char == char_to_count:
        count += 1
print(f"The character '{char_to_count}' occurs {count} times in the string.")
