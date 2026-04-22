"""
Reverse bits of a given 32 bits signed integer.


Example 1:

Input: n = 43261596

Output: 964176192

Explanation:

Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000
Example 2:

Input: n = 2147483644

Output: 1073741822

Explanation:

Integer	Binary
2147483644	01111111111111111111111111111100
1073741822	00111111111111111111111111111110
 

"""
def convertBinary(d):
    if d ==0 : 
        return 0
    
    else:
        return (d % 2 + 10 * convertBinary(d // 2))


def convertDecimal(b):
    d = 0
    base = 0
    temp = b
    while (temp):
        last = temp % 10
        d += last * pow(2,base)
        temp = temp // 10
        base += 1
    return d

   
    

def reverseBits(n):

    binary = convertBinary(n)
    reversed_bin = list(str(binary))
    if len(reversed_bin) < 32:
        reversed_bin = ['0'] * (32 - len(reversed_bin)) + reversed_bin
    reversed_bin = reversed_bin[::-1]

    # add 0's
    reversed_bin = int("".join(reversed_bin))
    decimal = convertDecimal(reversed_bin)
    return decimal
   




print(reverseBits(43261596)) # output 964176192
print(reverseBits(2147483644)) # output 1073741822