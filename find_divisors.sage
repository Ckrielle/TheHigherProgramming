def d(n):
	divisors = 1
	for fact in F:
		divisors *= fact[1]+1 # +1 is included because of the exponent 0
	return divisors

def s(n):
	"""
	s(n) = s(p^a * q^b * ...) = (p^0 + p^1 + ... + p^a) * (q^0 + q^1 + ... + q ^ b)
	"""
	divisor_sum = 1
	for fact in F:
		factor_sum = 0
		for exp in range(fact[1]+1):
			factor_sum += pow(fact[0], exp)
		divisor_sum *= factor_sum
	return divisor_sum

n = int(input("Give number: "))
F = list(factor(n))
dn = d(n)
sn = s(n)
print(f"Number of divisors is {dn}")
print(f"Sum of divisors is {sn}")
if (sn == 2*n): print(f"{n} is a perfect number")
