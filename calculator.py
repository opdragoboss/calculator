#
# DO NOT FORGET TO ADD COMMENTS!!!
# assignment: programming assignment 4
# author: Ethan Liu
# date: 3/2/2023
# file: calculator.py
# input: An infix string
# output: An evaulated expression
from stack import Stack
from t2 import ExpTree


def infix_to_postfix(infix):
    stack = Stack()
    num = ""
    postfix = ""

    for i in infix: #iterating through infix

        if i.isdigit() or i == ".":
            num += i
        # add number to postfix
        elif len(num) > 0:
            postfix += (num + ' ')
            num = ""

        if i == '(':
            stack.push('(')
        if i == ')':

            while stack.peek() != None and stack.peek() != '(':
                postfix += (stack.pop() + ' ')

            if stack.peek() == '(':
                stack.pop()

        if i in '^/*-+':
            #dictionary to implement pemdas
            pemdas = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 4, ')': 4}

            if stack.peek() != None and pemdas[i] > pemdas[stack.peek()]:
                stack.push(i)

            else:
                if stack.peek() != "(" and stack.peek() != None:
                    postfix += (stack.pop())
                stack.push(i)

    postfix += (num)
    stack1 = stack
    while stack1.peek() != None:
        postfix += " "
        postfix += stack.pop()

    return postfix
def calculate(infix):
    if infix == "":
        return ""
    a=1
    postfix = infix_to_postfix(infix)
    try:
        temp = float(postfix)
        return temp
    except ValueError:

        t = ExpTree.make_tree(postfix.split())
        return ExpTree.evaluate(t)


        return ExpTree.evaluate(t)

if __name__ == '__main__':
    # test infix_to_postfix function
    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'

    assert infix_to_postfix('5+2*3') == '5 2 3 * +'
    # test calculate function
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0
    print('Welcome to Calculator Program!')
    while True:
        print("Please enter your expression here. To quit enter 'quit' or 'q':")
        math = input()
        if (math == "quit") or math == "q":
            print("Goodbye!")
            break
        print(calculate(math))