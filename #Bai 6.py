#Bai 6
n = int(input("Nhập n: "))
temp = n
k = 0
t = n
while t > 0:
    k += 1
    t //= 10
tong = 0
while temp > 0:
    digit = temp % 10
    tong += digit ** k
    temp //= 10
if tong == n:
    print("Là số Armstrong")
else:
    print("Không phải số Armstrong")