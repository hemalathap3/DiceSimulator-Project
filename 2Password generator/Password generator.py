# we have to import string module
import string
import secrets    
# define password contains upper
def contains_upper(Password:str):
    for char in Password:
        if char.isupper():
            return True
    return False

# Password contains any special symbols
def contains_symbols(Password:str):
    for char in Password:
        if char in string.punctuation:
            return  True
    return False
    
# It contains length,symbols,upper
def generate_password(length:int,symbols:bool,upper:bool):   
    combination:str = string.ascii_lowercase + string.digits
    
    if symbols:
        combination += string.punctuation
    
# Assuming uppercase is a boolean variable indicating whether to include uppercase letters
    if uppercase:
        combination += string.ascii_uppercase

  # check the length of combination list        
    combination_length: int = len(combination)
# To pass the new value
    new_password:str = '' 
# Using range function
    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password
# generate newpassword,to changes the length
if __name__ == '__main__':
    for i in range(1,6):
        new_pass : str = generate_password('length=10','symbols=True','uppercase=True')
        specs:str = f'U:{contains_upper(new_pass)}, S:{contains_symbols(new_pass)}'
        
        print(f'{i} {new_pass}({specs})') 
             
        
