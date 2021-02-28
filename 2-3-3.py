n = int(input("Enter three digits (each digit for one pig): "))
pig1 = n // 100
pig2 = (n % 100) // 10
pig3 = (n % 100) % 10
total = pig1 + pig2 + pig3

print("Total bricks:", total)
print("Bricks per pig:", total // 3)
print("Remaining bricks:", total % 3)
print((total % 3) == 0)