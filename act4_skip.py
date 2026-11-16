total_sum=0

for n in range(1,51):
	if n%3==0:
		continue
	print(n, end=" ")
	total_sum += n
print()
print(f"Sum: {total_sum}")