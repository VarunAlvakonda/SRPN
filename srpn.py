from random import randint

# Imported this to be able to use random numbers

print("You can now start interacting with the SRPN calculator")

# This is a dictionary containing all the operators and when the dictionary is mentioned it returns the operation
operators = {
    "+": (lambda a, b: a + b),
    "-": (lambda a, b: a - b),
    "*": (lambda a, b: a * b),
    "/": (lambda a, b: a / b),
    "%": (lambda a, b: a % b),
    "^": (lambda a, b: a ** b)
}

# This is a list containing random numbers
random_nums = [1804289383,
               846930886,
               1681692777,
               1714636915,
               1957747793,
               424238335,
               719885386,
               1649760492,
               596516649,
               1189641421,
               1025202362,
               1350490027,
               783368690,
               1102520059,
               2044897763,
               1967513926,
               1365180540,
               1540383426,
               304089172,
               1303455736,
               35005211,
               521595368,
               1804289383,
               846930886,
               1681692777,
               1714636915,
               1957747793,
               424238335,
               719885386,
               1649760492,
               596516649,
               1189641421,
               1025202362,
               1350490027,
               783368690,
               1102520059,
               2044897763,
               1967513926,
               1365180540,
               1540383426,
               304089172,
               1303455736,
               35005211,
               521595368]


# This function checks the operators and determines their precedence
def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    return 0


# When the user input's 'r', this function returns a random number from the random_nums list and adds it to the stack
def randomise():
    value = randint(0, 44)
    return random_nums[value]


numbers = []
stack = []
ops = []


# This function carries out the main operations
def operation(number):
    operator = number
    op2 = stack.pop()
    if len(stack) == 0:
        print("Stack Underflow")
        return 0
    op1 = stack.pop()
    if operator == '/' and op2 == 0:
        print('Divide by 0')
        return 0
    elif len(stack) == 1:
        print("Stack Underflow")

    result = int(operators[operator](op1, op2))
    return result


# This function checks whether the user inputted a number or a letter and corresponds with the right output
def calculation(number):
    if number in operators:
        if len(stack) == 0:
            print("Stack Underflow")
        else:
            result = operation(number)
            if result > 2147483647:
                result = 2147483647
            elif result < -2147483647:
                result = -2147483648
            stack.append(result)
    elif number == 'r':
        stack.append(randomise())
    elif number == '=':
        print(stack[-1])
    elif number == 'd':
        for i in stack:
            print(i)
    elif str(abs(int(number))).isdigit():
        stack.append(int(number))
    if len(stack) >= 23:
        print("Stack Overflow")


# This function checks the operators and adds them in order of precedence
def isoperator(op):
    postfix = ''

    while True:
        if len(ops) == 0:
            ops.append(op)
            break
        else:
            pTC = precedence(op)
            pC = precedence(ops[-1])
            if pC >= pTC:
                ops.append(op)
                break
            else:
                postfix += ops.pop()


# This function takes an input and converts it from infix to postfix
def infix(y):
    postfix = ''
    val = 0
    i = 0
    for i in y:
        if i == '#':
            y.strip(i)
            while True:
                k = len(y) - 1
                while y[k] != '#':
                    y.strip(y[k])
                    k = k - 1
                    break
                if i == '#':
                    y.strip(i)
                    break
        if i in operators:
            isoperator(i)
        elif i == ' ':
            continue
        elif str(i).isdigit():
            val = (val * 10) + int(i)
            calculation(val)
            val = 0
        else:
            calculation(i)
    for op in ops:
        calculation(op)


# This takes the user input and is a while loop to make sure that the user can keep entering values
while True:
    x = str(input())
    # This is to check whether it should be converted to postfix from infix before calling the calculation function
    calculation(x)
