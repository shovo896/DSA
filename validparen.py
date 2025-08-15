class solution () : 
    def isvalid(self,s) :
        brackets = [] 
        pairs = {
            ')' : '(' ,
            '}' : '{' ,
            ']' : '[' ,
        }
        for char in s : 
            if char not in pairs : 
                brakets.append (char)
            elif not brakets or brakets [-1] != pairs[char] : 
                return False 
            else :
                brakets.pop()
            return len(brackets) == 0 