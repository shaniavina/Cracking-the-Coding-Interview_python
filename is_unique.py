
def isUnique1(s):
    used = {}
    for c in s:
        if c not in used:
            used[c] = 1
        else:
            return False
    return True       
    
    
def main():
    
    str = 'abfedfjlakg13450320qwedksaf'
    a = isUnique(str)
    print(a)

if __name__ == '__main__':
    main()
