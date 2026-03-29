#Bai 1
n = int(input("Nhập n: "))
a = 0
b = 1
i = 1
while i < n:
    a, b = b, a + b
    i += 1
print("Fibonacci thứ", n, "là:", b)