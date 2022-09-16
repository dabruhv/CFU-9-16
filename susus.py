import math

def pythagor(a, b, c):
    if a**2 + b**2 == c**2:
        print("good job you know stuff")
        return True
    elif a**2 + b**2 != c**2:
        print("ur bad at math")
        return False

print("question 1)")
print()
num1 = int(input("gimmie three numbers"))
num2 = int(input())
num3 = int(input())
num4 = num1 + num2 + num3

print("Average:", num4/3)

i = float(input("gimmie two more numbers"))
j = i
l = float(input())



print("square roots of the two numbers are ", math.sqrt(i), " and ",math.sqrt(l))
print("the first num to the second  ", j**l)
print()

print("question 2)")
a = int(input("give me number A"))
b = int(input("give me number B"))
c = int(input("give me number C"))
pythagor(a, b, c)
