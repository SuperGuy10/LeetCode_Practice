'''
Tag: Array; Difficulty: Easy.
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
'''

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
        	if i in {'[','{' ,'('}: #faster way than if i == '{'
        		stack.append(i)
        	else:
        		if len(stack) == 0:
        			return False
        		top = stack.pop()
        		if i == ']' and top != '[': #no need for ] to get in stack
        			return False
        		if i == '}' and top != '{':
        			return False
        		if i == ')' and top != '(':
        			return False
        if len(stack) != 0:
        	return False
        return True  #to avoid empty stack
