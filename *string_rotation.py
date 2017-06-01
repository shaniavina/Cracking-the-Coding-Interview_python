
def stringRotate(str1, str2):
    return isSubstring(str2, str1 + str1)

def isSubstring(str1, str2):
    i = 0
    j = 0
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i += 1
            j += 1
        else:
            if i == 0:
                j += 1
            else:
                return False
    return True
        
def main():
    
    str1, str2 = 'watermellon', 'ermellanwat'
    a = stringRotate(str1, str2)
    print(a)

if __name__ == '__main__':
    main()
