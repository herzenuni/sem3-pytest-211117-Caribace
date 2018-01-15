def digits_pow_sum(number):
	number = str(number)
	sum = 0
	for char in number:
		sum += int(char) ** 2
	return sum

def start():
	n = int(input("n = "))
	print("{} значные числа, сумма квадратов цифр которых делится на 17 без остатка :". format(n))
	for i in range(10 ** (n - 1), 10 ** n):
		if digits_pow_sum(i) % 17 == 0:
			print(i, end = ', ')
	print()

if __name__ == "__main__":
	start()
