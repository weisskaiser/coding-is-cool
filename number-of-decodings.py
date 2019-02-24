mapping = {str(i+1) for i in range(26)}

def print_run_time_nammed(name):
	def print_run_time(f):

		import time
		counter = 0
		def with_time(*args):

			start = time.time()
			nonlocal counter
			counter += 1

			ret = f(*args)

			counter -= 1
			if counter == 0:
				print(f"{name} runtime size {len(args[0])}: {round(time.time() - start,5):40f}")
			return ret

		return with_time
	return print_run_time

@print_run_time_nammed("Dynamic programming")
def dyn_decode(message):

	possibilities = [0 for _ in message]

	for i,c in enumerate(message):

		possibilities[i] = possibilities[i-1] if i > 0 else 1
		if i > 0 and (message[i-1]+message[i]) in mapping:
			possibilities[i] += 1
			if i-2 >= 0:
				possibilities[i] += possibilities[i-2] - 1

	return possibilities[-1]


@print_run_time_nammed("Brute force")
def decode(message):

	if not message:
		return 1

	one_char_pos = decode(message[1:])

	if len(message) > 1 and message[:2] in mapping:
		two_char_pos = decode(message[2:])
	else:
		two_char_pos = 0

	return one_char_pos + two_char_pos

assert decode('1111') == 5
assert dyn_decode('1111') == 5
assert decode('121') == 3
assert dyn_decode('121') == 3
assert decode('1234') == 3
assert dyn_decode('1234') == 3
assert decode('123456789') == 3
assert dyn_decode('123456789') == 3
message_long_time = "13421243214341341432134123421423142431221432124214124324214312"

#Brute force runtime size 62:                               219.254640
#Dynamic programming runtime size 62:                                 0.000000
assert decode(message_long_time) == dyn_decode(message_long_time)