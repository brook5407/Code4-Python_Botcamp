def calculate(num1, operator, num2):
	match operator:
		case '+':
			return num1 + num2
		case '-':
			return num1 - num2
		case '*':
			return num1 * num2
		case '/':
			return num1 / num2
		case default:
			return "Wrong Operator"


if __name__ == "__main__":
	print(calculate(10, "+", 10))
	print(calculate(10, "-", 10))
	print(calculate(10, "*", 10))
	print(calculate(10, "/", 10))

