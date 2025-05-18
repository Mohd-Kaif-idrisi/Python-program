def pelindrom(str):
    if len(str) < 1:
        return True
    else:
        if str[0] != str[-1]:
            return False
        return pelindrom(str[1:-1])
        

print(pelindrom("abcba"))        