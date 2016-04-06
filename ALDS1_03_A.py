def reverse_polish_notation(A):
    stack = []
    for i in A:
        if i.isdigit():
            stack.append(int(i))
        else:
            b = stack.pop()
            a = stack.pop()
            if i == "+":
                stack.append(a + b)
            elif i == "-":
                stack.append(a - b)
            elif i == "*":
                stack.append(a * b)
    print(stack[0])

if __name__ == '__main__':
    A = [i for i in input().split()]
    reverse_polish_notation(A)
