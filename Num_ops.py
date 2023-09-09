num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
division_result = num1 / num2
exponentiation_result = num1  num2

print("Sum:", num1, "+", num2, "=", sum_result)
print("Difference:", num1, "-", num2, "=", difference_result)
print("Product:", num1, "*", num2, "=", product_result)
print("Division:", num1, "/", num2, "=", division_result)

# Check if the second number is non-zero before calculating exponentiation
if num2 != 0:
    print("Exponentiation:", num1, "", num2, "=", exponentiation_result)
else:
    print("Exponentiation is undefined when the second number is 0.")

# Additional operations
# You can add more operations as needed.
