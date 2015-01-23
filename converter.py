translator = {0: 'A', 1: 'B', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: '0', 8: '1', 9: '2', 10: '3', 11: '4', 12: '5', 13: '6', 14: '7', 15: '8', 16: '9'}

# get top line from file, then delete

def get_line(file):
	line = open(file, 'r+')
	tweet_to_print = line.readline()
	return tweet_to_print

# convert string to integer of exactly 24 digits

def string_to_number(tweet):
	int_value = 0
	for c in ''.join(tweet):
		int_value += ord(c)
	if len(str(int_value)) == 24:
		return int_value
	elif len(str(int_value)) > 24:
		return cut_length(int_value)
	elif len(str(int_value)) < 24:
		while len(str(int_value)) < 24:
			int_value = int_value ** 2
		return cut_length(int_value)

# reduce length of integer to exactly 24 digits

def cut_length(number):
	string_number = str(number)
	while len(str(string_number)) > 24:
		string_number = string_number[:-1]
	return int(string_number)

# seperate digits into a list of integers

def number_to_list(number):
	number_list = []
	string_number = str(number)
	for n in string_number:
		number_list.append(n)
	number_list = map(int, number_list)
	return number_list

# take 4 digits, convert to binary if odd/even, then to integer, and append to hex list

def translate_to_binary(begin, end, integer_list, string, hex_list):
	digit_list = integer_list[begin:end]
	binary_list = []
	for n in digit_list:
		if n%2 == 0:
			binary_list.append('0')
		else:
			binary_list.append('1')
	if len(string) % 2 == 0:
		x = int(''.join(binary_list), 2) + 1
		hex_list.append(translator[x])
	else:
		x = int(''.join(binary_list), 2)
		hex_list.append(translator[x])