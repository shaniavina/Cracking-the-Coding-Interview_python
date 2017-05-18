
def checkPermutation1(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = ''.join(sorted(s1))   ####string sort() not work
    s2 = ''.join(sorted(s2))
    
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
        
    return True       

def checkPermutation2(s1, s2):
    if len(s1) != len(s2):
        return False  
    check = [0] * 128
    
    for c1 in s1:
        val = ord(c1) - ord('a')
        check[val] += 1
    for c2 in s2:
        val = ord(c2) - ord('a')
        check[val] -= 1
        if check[val] < 0:
            return False
    return True
def main():
    
    str1 = 'apple'
    str2 = 'pplae'
    a = checkPermutation2(str1, str2)
    print(a)

if __name__ == '__main__':
    main()
