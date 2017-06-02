stk1 =[]
sorted_stk1 = []

while stk1:
    tmp = stk1.pop()
    while sorted_stk1 and sorted_stk1.peek() > tmp:
        stk1.push(sorted_stk1.pop())
    sorted_stk1.push(tmp)
return sorted_stk1
