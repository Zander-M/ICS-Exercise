# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:52:13 2017

@author: Mebius
"""

import stack_student

"""
    PART 3 stack_C_1: Please write down the stack evaluation table entries here: (1 point)
    _________________________
    input  |  stack content
    _________________________
    7      |  7
    _________________________
    2      |  7, 2
    _________________________
    +      |  9
    _________________________
    5      |
    _________________________
    *      |
    _________________________
    3      |
    _________________________
    +      |
    _________________________
    10     |
    _________________________
    -      |
    _________________________
"""

"""
    PART 3 stack_C_2: Stack machine implementation
"""
class StackMachine:
    """StackMachine: a stack-based calculator

    Methods:
        .init():
            initialize an internal stack
        .is_op(op):
            return True if op is '+', '-', '*', '/'
        .is_operand(x):
            return True if x is an integer
        .do_op(x, y, op):
            perform x 'op' y; e.g. do_op(3, 2, '-') produces 1
        .feed(x):
            if x is an operand, push to stack
            else pop two off the stack, compute and push to stack
        .peek():
            return top of the stack
        .print_stack():
            print the content of the stack
    """

    def __init__(self):
        self.stack = stack_student.Stack()

    def is_op(self, op):
        """ if op is either one of '+', '-', '*', '/' return True
                return False otherwise """
        #------your code here-------#
        return True if op in ['+', '-', '*', '/'] else False

    def is_operand(self, x):
        """ if x is an integer, return True"""
        #------your code here-------#
        return True if type(x) == int else False
    
    def do_op(self, x, y, op):
        """modify: do the computation for '+', '-', '*', '/'
                 example: if op is '+' then return x + y"""
        #------your code here-------#
        if op == '+':
            self.stack.push(x + y)
            return x + y
        elif op == '-':
            self.stack.push(x - y)
            return x - y
        elif op == '*':
            self.stack.push(x * y)
            return x * y
        elif op == '/':
            self.stack.push(x / y)
            return x / y

    def feed(self, x):
        """     if x is an operand, push it onto the stack
                else if it's an operator, pop two items and
                 compute the result (using self.do_op method),
                 push it back onto the stack  """
        #------your code here-------#
        if type(x) == int:
            self.stack.push(x)
        elif x in ['+', '-', '*', '/']:
            a = self.stack.pop()
            b = self.stack.pop()
            self.do_op(a, b, x)
        return

    def peek(self):
        return self.stack.peek()

    def print_stack(self):
        print(self.stack)
        return


## DO NOT EDIT THE MAIN FUNCTION
if __name__ == "__main__":
    exp = [7, 2, '+', 5, '*', 3, '+', 10, '-']
    stack_machine = StackMachine()
    for x in exp:
        stack_machine.feed(x)
        stack_machine.print_stack()

