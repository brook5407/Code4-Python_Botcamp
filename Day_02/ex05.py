def check_string(str):
	if (str.find("The") != -1):
		return "Yes!"
	else:
		return "No!"


if __name__ == "__main__":
	str1 = 'The'
	str2 = 'Thumbs up'
	str3 = 'Theatre can be boring'
	print(check_string(str1))
	print(check_string(str2))
	print(check_string(str3))
