str1 = input("Enter the first string: ").replace(" ", "").lower()
str2 = input("Enter the second string: ").replace(" ", "").lower()
# Check lengths
if len(str1) != len(str2):
    print("The strings are not anagrams.")
else:
    # use sorted function
    if sorted(str1) == sorted(str2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")
