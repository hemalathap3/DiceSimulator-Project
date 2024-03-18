from random import randint
lower_number,higher_number = (1,9)
random_number:int = randint(lower_number,higher_number)
print('guess the number it is in the range{lower_number} to {higher_number}')

while True:
    try:
        user_guess:int = int(input('guess:'))
    except ValueError as e:
        print('please enter a valid number:')
        continue
    
    if user_guess>random_number:
        print('The number is lower')
    elif user_guess<random_number:
        print('The number is higher')  
    else:
        print('You guessed')   
        break   
            
    
