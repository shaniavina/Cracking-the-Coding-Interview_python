
def oneAway(str1, str2):
    count = 1
    long = ''
    short = ''
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count -= 1
                if count < 0:
                    return False
    if len(str1) - len(str2) == 1:
        long = str1
        short = str2
    elif len(str2) - len(str1) == 1:
        long = str2
        short = str1
    else:
        return False
    i = 0
    j = 0
    while i < len(long) and j < len(short):
        if long[i] != short[j]:
            if count <= 0:
                return False
            count -= 1
            i += 1
        else:
            i += 1
            j += 1
            
    return True  
                
                
def main():
    
    str1, str2 = 'bale', 'plek'
    a = oneAway(str1, str2)
    print(a)

if __name__ == '__main__':
    main()
