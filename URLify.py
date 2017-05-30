
def URLify(str, cnt):
    res = []
    res_cnt = 0
    for s in str:
        if s != ' ':
            res.append(s)
        else:
            if res_cnt < cnt:
                res.append('%20')
            else:
                break
        res_cnt += 1
    return ''.join(res)
def main():
    
    str, cnt = 'i have an apple   ', 17
    a = URLify(str, cnt)
    print(a)

if __name__ == '__main__':
    main()
