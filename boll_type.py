comparison_result: bool = 3 < 5
print(comparison_result)

comparison : bool = 5 > 5
print(comparison)

comparison_1 : bool = 5 != 5
print(comparison_1)

comparison_2 : bool = 5 <= 5
comparison_3 : bool = 5 >= 5
print(comparison_2, "/n", comparison_3)

result = True and True or False #був True
result_1 = (True and True) or not False
result_2 = not True or True and not False
result_3 = True or True and not False
result_4 = True and (True or False)
print(result_4)
print(result_3)
print(result_2)
print(result_1)

bool_none = "bool_non"
another_result = print(7)
print(another_result, type(another_result), id(another_result))
print(another_result == another_result)

sum_str = " "
sum_result = 10 - 1
print (sum_str, sum_result, sum_result == sum_str)

sum_bool = True or False
print(sum_bool)
h = print("Today is rainy")
print(sum_bool == h )
