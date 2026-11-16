size=int(input("Size (1-10): "))
while size < 1 or size > 10:
    print("Invalid size! please enter a number between 1 and 10.")
    size=int(input("Size (1-10): "))

print()

for row in range(1, size + 1):
    for col in range(1, size + 1):
        print(f"{row * col:4}", end=" ")
    print() 
