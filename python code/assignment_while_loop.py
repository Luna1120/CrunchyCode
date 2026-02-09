from loguru import logger
a = int(input(f"Please enter the number: "))
operator1 = input(f"Please select the operator (+,-,*,/):")
while True:
    b = int(input(f"Please select the next number: "))
    if operator1 == '+':
        result = a + b
    elif operator1 == '-':
        result = a - b
    elif operator1 == '*':
        result = a * b
    else:
        result = a / b
    a = result  
    print(result)
    operator1 = input(f"Please select the operator (+,-,*,/):")  