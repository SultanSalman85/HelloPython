print ("bitsum operation exercise")


def decimalToBinary(num):
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')

number1 = int(input("Enter first decimal number: "))
number2 = int(input("Enter second decimal number: "))

print (number1,  " add by ",  number2 , "equals : ")
decimalToBinary(number1+number2)

print ("\n")

print (number1,  " minus by ",  number2 , "equals : ")
decimalToBinary(number1-number2)

print ("\n")

print (number1,  " times by ",  number2 , "equals : ")
decimalToBinary(number1*number2)

print ("\n")

    #the output is still a decimal number (^o*)
print (number1,  " divided by ",  number2 , "equals : ")
decimalToBinary(number1/number2)

print ("\n")

        #doesn't works because it doesn't understand the "~" thing (-_-')

    #print (number1,  " complement by ",  number2 , "equals : ")
    #decimalToBinary(number1 ~ number2)

print (number1,  " and by ",  number2 , "equals : ")
decimalToBinary(number1&number2)

print ("\n")

print (number1,  " or by ",  number2 , "equals : ")
decimalToBinary(number1|number2)

print ("\n")

print (number1,  " Xor by ",  number2 , "equals : ")
decimalToBinary(number1^number2)

print ("\n")

print (number1,  " rightsifted by ",  number2 , "equals : ")
decimalToBinary(number1>>number2)

print ("\n")

print (number1,  " leftsifted by ",  number2 , "equals : ")
decimalToBinary(number1<<number2)

print ("\n")

print ("thank You!")

