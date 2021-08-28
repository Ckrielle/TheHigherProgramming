import time


"""
I experimented a lot with this Class, going back and forth on whether I
should add it or nor. First problem was that __init__ messed up the
two numbers, and so I got rid of it opting for passing arguments. I tried
using @staticmethod for the methods, but the last recursive one had some
troubles and needed self, so I kept it for uniformity. I went with it
mainly because of the contained scope. Ok after I understood that this doesn't
need to be .sage and converted it to python the class becomes kinda obsolete,
but i'll keep it cause I'm bored to change it
"""
class GreatestCommonDivisor:
	def gcd1(self, a: int, b: int) -> int:
		"""
		1st attempt
		a = qb + c  (c = a - qb)
		b = rc + d
		...
		"""
		while b != 0:
			q = 1
			while q * b < a - b:
				q += 1
			temp = b
			b = a - (q * temp)
			a = temp
		return a

	def gcd2(self, a: int, b: int) -> int:
		"""
		2nd attempt
		a = qb + c  (c = a - qb)
		b = rc + d
		...
		"""
		flag = True
		while flag:
			q = a // b
			temp = a - (q * b)
			if temp == 0:
				flag = False
			else:
				c = temp
				a = b
				b = c
		return c

	def gcd3(self, a: int, b: int) -> int:
		"""
		3rd attempt
		"""
		while b != 0:
			q = a // b
			temp = b
			b = a - (q * b)
			a = temp
		return a

	def gcd4(self, a: int, b: int) -> int:
		"""
		4th attempt
		"""
		while b != 0:
			c = a % b
			a = b
			b = c
		return a

	def gcd5(self, a: int, b: int) -> int:
		"""
		Wikipedia code
		"""
		while b != 0:
			temp = b
			b = a % b
			a = temp
		return a

	def gcd6(self, a: int, b: int) -> int:
		if b == 0: return a
		else: return self.gcd6(b, a % b)

    def gcd7(self, a: int, b: int) -> int:
            if a == 0: return b
            elif b == 0: return a
            elif a == b: return a
            elif a > b: return self.gcd7(a - b, b)
            else: return self.gcd7(a, b - a)


if __name__ == "__main__":
	print("Give two numbers")
	nums = [int(x) for x in input().split()]
	n1, n2 = max(nums), min(nums)
	gcd = GreatestCommonDivisor()
	gcd_list = [m for m in dir(GreatestCommonDivisor) if '__' not in m]
	for m in gcd_list:
		s = time.time()
		print(getattr(gcd, m)(n1, n2))
		print(f"{m} time is {time.time()-s}")
