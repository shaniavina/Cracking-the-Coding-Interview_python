#global str
def stringCompress(string):
    res = [string[0]]
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            res.append(str(count))
            count = 1
            res.append(string[i])
    res.append(str(count))
    if len(res) >= len(string):
        return string
    else:
        return ''.join(res)
def main():
    
    string= 'abc'
    a = stringCompress(string)
    print(a)

if __name__ == '__main__':
    main()
