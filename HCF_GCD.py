num1, num2 = map(int, input("Enter two numbers separated by a space: ").split())
min_num = min(num1, num2)
hcf = 1
for i in range(2, min_num + 1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print("The HCF of", num1, "and", num2, "is:", hcf)
