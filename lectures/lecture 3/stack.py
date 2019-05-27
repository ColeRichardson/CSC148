class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError
        else:
            return self._items.pop()

    def is_empty(self):
        if self._items == []:
            return True
        else:
            return False


class EmptyStackError(Exception):
    """an exception raised when the stack contains no items"""
    pass

def get_top(s):
    """

    :param s:
    :return:
    precondition s is not empty
    """
    top = s.pop()
    s.push(top)
    return top

def remove_items(s):
    while not s.is_empty():
        curr = s.pop()
    s.push(curr)

def size(s):
    count = 0
    curr_stack = Stack()
    while not s.is_empty():
        curr_stack.push(s.pop())
        count += 1
    while not curr_stack.is_empty():
        s.push(curr_stack.pop())
    return count

def is_balanced(s:str):
    bracket_stack = Stack()
    for char in s:
        if char == '(':
            bracket_stack.push(char)
        elif char == ')':
            if bracket_stack.is_empty():
                return False
            bracket_stack.pop()
            
    return bracket_stack.is_empty()

