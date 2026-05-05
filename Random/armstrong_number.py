
import math


def is_armstrong(num: int) -> bool:

    final =0 
    temp = num
    num_digits = math.floor(math.log10(num)) + 1  
    while(num > 0):
        final += (num % 10 ) ** num_digits 
        print(final)
        num = num // 10


    if final == temp:
        return True
    

    
    return False


# These "asserts" are used for self-checking
assert is_armstrong(153) == True
assert is_armstrong(370) == True
assert is_armstrong(947) == False
assert is_armstrong(371) == True
assert is_armstrong(407) == True
assert is_armstrong(163) == False
assert is_armstrong(100) == False
assert is_armstrong(8208) == True
assert is_armstrong(930) == False
assert is_armstrong(4) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
