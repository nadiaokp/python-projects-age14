print("👋 Hello! Welcome to The Calculator")

name = input("What's your name?: ")

num = int(input('Give me your first digit: '))

num_2 = int(input('Give me your second digit: '))

procedure = input('What procedure would you like? Addition? Subtraction? Division? Multiplication? Average? : ').lower()

if procedure == 'addition':
    print(f'Okay, {name}')
    print(f'{num} + {num_2} = {num + num_2}')
    
if procedure == 'subtraction':
    print(f'Okay, {name}')
    print(f'{num} - {num_2} = {num - num_2}')
    
if procedure == 'division':
    print(f'Okay, {name}')
    print(f'{num} / {num_2} = {num/num_2}')
    
if procedure == 'multiplication':
    print(f'Okay, {name}')
    print(f'{num} * {num_2} = {num * num_2}')
    
if procedure == 'average':
    print(f'Okay, {name}')
    print(f'The average of {num} and {num_2} is {(num + num_2)/2}')