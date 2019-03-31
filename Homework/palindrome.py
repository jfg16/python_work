dict1={}

def ReadStrings(counter,string):
    dict1[counter] = string

print("Enter the strings: ", end="")
counter = 0

while True:
    palin = input("")
    if palin == 'Done':
        break
    else:
        temp = palin
        palin = palin.lower()
        palin = palin.replace(" ", "")
        rev = ''.join(reversed(palin))
        if rev==palin:
            counter = counter + 1
            ReadStrings(counter,temp)

print("The Palindromes are: ")
for lett,case in dict1.items():
    print(" " + str(lett) + ": "+str(case))