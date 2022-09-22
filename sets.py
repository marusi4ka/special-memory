number_1 = set(input('number_1: '))
number_2 = set(input('number_2: '))
print(number_1, number_2)

number_3 = number_2.union(number_1)
print(f'{number_3=}, id{(number_3)=}')

# number_2 = {input('number_4: ')}
difference = set.difference(number_2)
print(f"{difference=}, {id(difference)=}")

# a = set(input('number_1: '))
# b = set(input('number_2: '))
# print(a, b)
# d = a.intersection(b)
# print(f'{d=}, id{(d)=}')
# difference = a.difference(b)
# print(f"{difference=}, {id(difference)=}")


Emily = {'dog', '32', 'rabbit', 'girls' }
Sam = {'2', 'family', 'random', 'Dog'}
Tobi = {'words', 'deal', 'rabbit', '2', '12'}
result = Emily | Sam | Tobi
result_2 = Emily - Sam - Tobi
result_3 = Emily ^ Sam ^ Tobi
print(f"{type(result)=}, {result=}")
print(f"{result_2=}, {id(result_2)=}")
print(f"{result_3=}, {id(result_3)=}")

Kate = {'rabbit', '463', 'home', 'pen'}
Alex = {'Blue', 'Look', 'COOL', '190836'}
Mary = {'home', '463', 'rabbit', '2', '12'}
result_1 = Kate & Mary & Alex
print(f"{type(result_1)=}, {result_1=}")
print(f"Kate & Mary & Alex --> {Kate & Mary & Alex}")
