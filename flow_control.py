# # operand_1: str = input('hello baby ')  # input always return string
# # operand_1 = int(operand_1)

operand_1: int = int(input('input number one: '))
operand_2: int = int(input('input number two: '))

number_1 = float(operand_1) if '.' in operand_1 else int(operand_1)
number_2 = float(operand_2) if '.' in operand_2 else int(operand_2)

sign: str = input('input sign ')  # +,- .etc


if sign == '*':
    result = operand_1 * operand_2
elif sign == '-':
    result = operand_1 - operand_2
elif sign == '+':
    result = operand_1 + operand_2
elif sign == '**':
    result = operand_1 ** operand_2
elif sign == '/':
    result = operand_1 / operand_2
print(result)

try:
    print(result)
except:
    print("You provide unexpected sign")
