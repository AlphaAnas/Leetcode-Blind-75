
# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

 
# def dec_to_binary(dec):
    
#     if dec == 0:
#         return dec

#     final = []
#     while (dec > 1):
#         final.append(dec % 2)

#         dec = dec // 2
#     return final

def hammingWeight(n):

    b = bin(n)[2:] 
    # print(type(b))
    ones = [i for i in b if i == "1"]
    return len(ones)

print(hammingWeight(128)) # output 1
print(hammingWeight(2147483645)) # output 30
print(hammingWeight(11)) # output 3