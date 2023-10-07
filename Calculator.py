#Calculator

def Calculator():
    num_1 = int(input('Enter The First Number: '))
    num_2 = int(input('Enter The Second Number: '))
    operation = input('''Choose + for Addition
Choose - for Substraction
Choose x for Mupltiplication
Choose / for Division
Choose The Operator: ''')
    if operation == '+':
        print(num_1 ,'+', num_2 ,'=',num_1+num_2)
    elif operation == '-':
        print(num_1 ,'-' ,num_2 ,'=',num_1-num_2)
    elif operation == 'x':
        print(num_1, 'x', num_2 ,'=',num_1*num_2)
    elif operation == '/':
        print(num_1 ,"/" ,num_2, '=',num_1/num_2)
    else:
        print('!! ERROR !!')
Calculator()
