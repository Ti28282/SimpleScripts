from random import choice
import string

def Generation(length:int, numbers:bool, letters:bool, symbols:bool) -> str:
    result = ""
    characters = ""
    
    if numbers:
        characters += string.digits

    if letters:
        characters += string.ascii_letters

    if symbols:
        characters += string.punctuation
    
    if characters:
        
        for _ in range(length):
            result += choice(characters)
    
    else:
        raise ValueError("At least one of the parameters (numbers, letters, symbols) must be True")
    
    return result
