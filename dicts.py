asciiDict = {i: chr(i) for i in range(128)}
print(asciiDict)


string = input("Enter a string: ")
srt = string.replace(" ", "")
if srt.isalpha():
    print(srt)
else:
    print("Only letters without spase: this is not working")

s = 0
print("Enter your password: ")
password = int(input())
while s == password:
    print("Your password is right")
    print(password)






