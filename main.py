a = int(input("number to convert : "))
base = int(input("to base : "))

# Calcul of pounds
nbOfDigits = 0
pounds = []
while(a >= base**nbOfDigits):
    pounds.append(base**nbOfDigits)
    nbOfDigits += 1
pounds.reverse()

# Conversion
result = []
for i in range(len(pounds)):
    result.append(divmod(a, pounds[i])[0])
    a = divmod(a, pounds[i])[1]
print(result)