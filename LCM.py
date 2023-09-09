num1, num2 = map(int, input("Enter two numbers separated by a space: ").split())
max_num = max(num1, num2)

lcm = max_num

while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    lcm += max_num
print("The LCM of", num1, "and", num2, "is:", lcm)
