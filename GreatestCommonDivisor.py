
def gcdOfStrings(str1: str, str2: str):

        # check if substr of b is also a substr of a

        s_len = len(str2) if len(str2) < len(str1) else len(str1)
  
        if len(str1) >= len(str2):
            max_str, min_str = str1, str2
        else:
            max_str, min_str = str2, str1

        final = ""


        for i in range(s_len, 0, -1):
            if (len(max_str) % i == 0) and (len(min_str) % i == 0):
                n1, n2 = len(max_str) // i, len(min_str) // i
                base = min_str[ : i ]
                cond1 = base * n1 == max_str
                cond2 = base * n2 == min_str

                if cond1 and cond2:
                    final = base
                    break
            

        return final
            
              
    

print(gcdOfStrings("ABCABC", "ABC"))
print(gcdOfStrings("ABABAB", "ABAB"))
print(gcdOfStrings("LEET", "CODE"))
print(gcdOfStrings("AAAAAB", "AAA"))



        