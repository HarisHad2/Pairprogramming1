def factor_group(num):
	return 'odd' if (num ** 0.5)%1 == 0 else 'even'

print(factor_group(100))    