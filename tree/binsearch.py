import random
import time
import functools

def timethis(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print('elapsed time is {}'.format(end-start))
		return result
	return wrapper

@timethis
def binsearch(list_, target):
	length = len(list_) - 1
	start = 0
	while start <= length:

		mid = (length + start) // 2
		if list_[mid] > target:
			length = mid - 1
		elif list_[mid] < target:
			start = mid + 1
		else:
			return mid
	return -1

if __name__ == '__main__':
	list_ = list(range(1000000))
	list_ = sorted([random.choice(list_) for i in range(100000)])
	target = random.choice(list_)

	result = binsearch(list_, target)
	print('the result is {}'.format(target))

	