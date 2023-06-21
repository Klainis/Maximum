

def palindrom(s):
    
    if len(s)%2==0:
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2:] 
        if s1 == s2[::-1]:
            return True
        else:
            return False
    elif  len(s)%2!=0:
        s1 = s[:(len(s)-1)//2]
        s2 = s[(len(s)-1)//2+1:]
        if s1 == s2[::-1]:
            return True 
        else:
            return False

print(palindrom('tenet'))
