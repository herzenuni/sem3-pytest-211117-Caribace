from 1 import digits_sum

def factory(number, my_sum):
	def abstract_test():
		assert digits_sum(number) == my_sum
	return abstract_test

test_1 = factory(123, 6)
test_2 = factory(1234, 10)
