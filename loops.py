user_letters = input("input letters: " )
print(user_letters)

# 2 задание

user_input = input("input letters 2: ")
result_user = ""
index = 0
while index < len(user_input):
    print(user_input[index])
    if user_input[index] == user_input[index].upper():
        result_user = result_user + user_input[index]

    index += 1
print(result_user)

# 3 задание

object_for_enumerate = input('index words: ')
for index, element in enumerate(object_for_enumerate):
    if element == ' ':
        print(f"{index=}|{element=}")

# 4 задание

# import re
#
#     user_input = input("letters: ")
#
#     result = ""
#     for i in user_input:
#         print(i)
#         print(result)
#
#         if re.match(r'^['a', 'e', 'i', 'o', 'u', 'y']', i):
#             result = result + i
#     print(result)
#     или решение ниже

letters = {'A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y'}
a = set(input("Input text "))
b = a & letters
print(b)

# # 5 задание

user_input = input("input letters: ")
result_user = ""
index = 0
while index < len(user_input):
    print(user_input[index])
    if user_input[index] == user_input[index].isalnum():
        result_user = result_user + user_input[index]

    index += 1
print(result_user)

# # 6 задание

input_str = input("repeat: ")
i = 0
while i < 3:
    print(input_str)
    i += 1
#
#


