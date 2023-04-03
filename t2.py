#
# DO NOT FORGET TO ADD COMMENTS!!!
# assignment: programming assignment 4
# author: Ethan Liu
# date: 3/2/2023
# file: t2.py
# input: expression string
# output: expression tree

from stack import Stack


class BinaryTree:
    def __init__(self, rootObj=None):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def __str__(self):
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s


class ExpTree(BinaryTree):

    # Create the exp tree
    def make_tree(postfix):
        stack = Stack()
        possible = "^*/-+"



        for i in postfix:
            if i.isdigit() or '.' in i:
                stack.push(ExpTree(i))
            if i in possible:
                temp = ExpTree(i)
                temp.rightChild = stack.pop()
                temp.leftChild = stack.pop()
                stack.push(temp)

        return stack.pop()

    def preorder(tree):
        s = ''
        if tree != None:
            s = tree.getRootVal()
            s += ExpTree.preorder(tree.getLeftChild())
            s += ExpTree.preorder(tree.getRightChild())
        return s

    def inorder(tree, s=''):

        s = ''
        possible = "^*/-+"
        if tree != None:
            if tree.getRootVal() in possible:
                s += '('
            s += ExpTree.inorder(tree.getLeftChild())
            s += tree.getRootVal()
            s += ExpTree.inorder(tree.getRightChild())
            if tree.getRootVal() in possible:
                s += ')'
        return s

    def postorder(tree):

        s = ''

        if tree != None:
            s += ExpTree.postorder(tree.getLeftChild())
            s += ExpTree.postorder(tree.getRightChild())
            s += tree.getRootVal()
        return s

    def evaluate(tree):

        possible = "^*/-+"


        if tree == None:
            return None
        else:
            if tree.getRootVal() not in possible:
                return float(tree.getRootVal())
            right = ExpTree.evaluate(tree.getRightChild())
            left = ExpTree.evaluate(tree.getLeftChild())



            root = tree.getRootVal()
            if root == "/":
                return left / right
            elif root == "*":
                return left * right
            elif root == "-":
                return left - right
            elif root == "+":
                return left + right


    def __str__(self):
        return ExpTree.inorder(self)


# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':
    # test a BinaryTree

    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild() == None
    assert r.getRightChild() == None
    assert str(r) == 'a()()'

    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'

    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'

    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'

    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'

    # test an ExpTree

    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '(5+(2*3))'
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    assert ExpTree.preorder(tree) == '+5*23'
    assert ExpTree.evaluate(tree) == 11.0

    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0