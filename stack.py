#
# DO NOT FORGET TO ADD COMMENTS!!!
# assignment: programming assignment 4
# author: Ethan Liu
# date: 3/2/2023
# file: stack.py
# input:
# output: stack object
class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        a = len(self.stack)
        return a == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)


# a driver program for class Stack
if __name__ == '__main__':

    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)

    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]
    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())
    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None