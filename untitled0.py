# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 12:47:27 2021

@author: User
"""

import sys

def isBalanced(s):
    stack = []
 
    for letter in s:
        if letter == '{':
            stack.append(1)
        elif letter == '[':
            stack.append(2)
        elif letter == '(':
            stack.append(3)
        elif letter == '}':
            if len(stack) == 0:
                return False
            if stack.pop() != 1:
                return False
        elif letter == ']':
            if len(stack) == 0:
                return False
            if stack.pop() != 2:
                return False
        elif letter == ')':
            if len(stack) == 0:
                return False
            if stack.pop() != 3:
                return False
 
    return len(stack) == 0


for I in range(5):
    brackets = input("ENTER BRACKETS: ").strip()
    result = isBalanced(brackets)
    if result is True:
        print('YES')
    else:
        print('NO')
        

def is_balanced_expression(test_str):
	stack = list()
	open_brackets = ["(", "{", "["] 
	closing_brackets = [")", "}", "]"]

	for ch in test_str:
		if ch in open_brackets:
			stack.append(ch)
		elif ch in closing_brackets:
			if stack and open_brackets[closing_brackets.index(ch)] == stack[-1]:
				stack.pop()
			else:
				return False
	return bool(stack) is False

for i in range(3):
    x = input("ENTER INPUTS ")
    result = is_balanced_expression(x)
    if result is True:
        print('YES')
    else:
        print('NO')
        

arr = []
for i in range(0, 2):
    # arr[i] = input("ENTER STUDENT {} NAME".format(i+1))
    arr.append([])
    for j in range(0, 2):
        # exam = input("ENTER EXAM {} NAME".format(j+1))
        # arr[i].append(exam)
        for k in range(0, 2):
            parts = input("ENTER PARTS {} NAME".format(j+1))
            arr[i][j][k] = parts

print(arr)