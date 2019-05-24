from stack import Stack

if __name__ == "__main__":
    test_stack = Stack()
    test_stack.push("Hello")
    test_stack.pop()
    check = True
    color_stack = Stack()
    while check:
        color = input("enter your favourite color, once your done, type done")
        if color == 'done':
            check = False
            break
        else:
            color_stack.push(color)

    while not color_stack.is_empty():
        print(color_stack.pop())
