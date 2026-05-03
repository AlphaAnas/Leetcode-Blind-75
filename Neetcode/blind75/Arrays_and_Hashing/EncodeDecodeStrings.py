
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
import string


def encode( strs: list[str]) -> str:

    encoded : str = ""

    for word in strs:
        encoded += "SOW" + word + "EOW"

    return encoded

def decode( s: str) -> list[str]:


    decoded = []

    word = ""
    temp = s.split("EOW")
  
    for words in temp:
            
            if len(words) > 0:
                    
                word = words.split("SOW")[1]
                decoded.append(word)
                word = ""
            

    return decoded


original =["we","say",":","yes","!@#$%^&*()"]
encoded = encode(original  ) 
decoded = decode(encoded)
print("encoded: ", encoded)
print("decoded: ", decoded)
original = ["Hello","World"]
encoded = encode(original  ) # output ["Hello","World"]V
decoded = decode(encoded)
print("encoded: ", encoded)
print("decoded: ", decoded)
assert decoded == original
original = []
encoded = encode(original) # output [""]
decoded = decode(encoded)
assert decoded == original
