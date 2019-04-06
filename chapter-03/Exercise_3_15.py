# Exercise 3.15

firstNumber = input("Now, please enter the first number: >>> ")
secondNumber = input("Now, please enter the second number: >>> ")
operator = raw_input("Please enter A S M or D: >>> ")
if operator == 'A':
    result = firstNumber + secondNumber
elif operator == 'S':
    result = firstNumber - secondNumber
elif operator == 'M':
    result = firstNumber * secondNumber
elif operator == "D":
    if secondNumber != 0:
        result = firstNumber / float(secondNumber)
    else:
        result = "NaN. Can't be divided by zero."
else:
    result = "???????"
print "The result is", result
