def calculate():
    operation = input('''
add for addition
sub for subtraction
mul for multiplication
div for division
''')

    num_1 = int(input())
    num_2 = int(input())

    if operation == 'add':
        print('{} + {} = {}'.format(num_1, num_2,num_1 + num_2))
       

    elif operation == 'sub':
        print('{} - {} = {}'.format(num_1, num_2,num_1 - num_2))
       

    elif operation == 'mul':
        print('{} * {} = {}'.format(num_1, num_2,  num_1 * num_2))
      

    elif operation == 'div':
        print('{} / {} = {}'.format(num_1, num_2,num_1 / num_2))
       

    else:
        print('invalid input.')
calculate() 
