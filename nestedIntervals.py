"""
Given a mathematical equations as a string, return whether or not the brackets
are appropriately balanced.
"""
# O(n)
def solution(equation):
  mapping = {
    '}': '{',
    ')': '(',
    ']': '['
  }
  closing = {')', ']', '}'}
  opening = {'(', '[', '{'}
  stack = []

  for ch in equation:
    if ch in opening:
      stack.append(ch)
    elif ch in closing:
      if not stack:
        return False
      top = stack.pop()
      if top != mapping[ch]:
        return False
  
  return not stack
        
    

print(solution("(3+9{12+4})(25)")) # true
print(solution("3+9{12+4})(25)")) # false
