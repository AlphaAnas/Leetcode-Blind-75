# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.


def isValid( s: str) -> bool:

        stack = []
        b_dict = { ")" : "(", "]" : "[", "}" : "{" }
        for b in s :


            if b in b_dict: # if its a closing bracket    
                if stack and stack[-1] == b_dict[b]:
                    stack.pop()

                else:
                    return False
            else: # add to stack all the opening brackets
                 stack.append(b)
        return True



          
        


        return len(stack) == 0


print(isValid(s = "[]")) # output true
print(isValid(s = "([{}])")) # output true
print(isValid(s = "[(])")) # output false
