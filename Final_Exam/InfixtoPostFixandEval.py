from Stack import Stack

def infix_to_postfix(inf):
    precedence={'+':1,'-':1,'*':2,'/':2,'^':3}
    output=[]
    stack=Stack(10)
    infix=inf.split()

    for char in infix:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() !='(':
                output.append(stack.pop())
            stack.pop()
        else:
            while not stack.is_empty() and stack.peek() != '(' and precedence[stack.peek()] >= precedence[char]:
                output.append(stack.pop())
            stack.push(char)

    
    while not stack.is_empty():
        output.append(stack.pop())

    return ' '.join(output)

ex=" 3 + 2 * 4 "

x=infix_to_postfix(ex)
print(x)



def evaluation(arr):
    token=arr.split()
    res=[]
    print(token)
    s=Stack(10)

    for i in token:
        if i.isdigit():
            s.push(int(i))
        else:
            right=s.pop()
            left=s.pop()

            if i == '+':
                res=left +right
                s.push(int(res))
            elif i == '-':
                res=left - right
                s.push(int(res))
            elif i == '*':
                res=left  * right
                s.push(int(res))
            elif i == '/':
                res=left / right
                s.push(int(res))
    return s.pop()
    


print(evaluation(x))