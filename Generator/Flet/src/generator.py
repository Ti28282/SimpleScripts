from random import choice
import string

def Generation(length:int, numbers:bool, letters:bool, symbols:bool) -> None:

        if numbers and letters and symbols:
            result = ""
            for _ in range(length):
                
                result += choice(string.digits + string.ascii_letters + string.punctuation)
            return result
        
        elif numbers and letters:
            result = ""
            for _ in range(length):
                
                result += choice(string.digits + string.ascii_letters)
            return result

        elif numbers:
            result = ""
            for _ in range(length):
                
                result += choice(string.digits)
            return result
        
        elif letters:
            result = ""
            for _ in range(length):
                
                result += choice(string.ascii_letters)
            return result

        elif symbols:
            result = ""
            for _ in range(length):
                
                result += choice(string.punctuation)
            return result
        