def count_vowel(str):
    count = 0
    for i in range(0,len(str)):
        if(str[i] == 'a' or str[i] == 'e' or str[i]== 'i' or str[i] == 'o' or str[i] == 'u'):
            count=1+count
    print(count)
    
count_vowel("kaif is a good boy")    



