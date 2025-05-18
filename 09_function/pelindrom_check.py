def pelindrom(str):
    left = 0
    right = len(str) - 1
    while left < right:
        if str[left] != str[right]:
           return False  
        left += 1
        right -= 1     
    return True

print(pelindrom("abcdcba"))        
    
    