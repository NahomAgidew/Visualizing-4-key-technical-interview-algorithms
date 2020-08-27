"""
Given a string and a set of characters, find the length of the smallest substring that contains
all of the characters.
"""
# O(n) time
def solution(string, characters):
  minLength = float('inf')
  left = right = 0
  characterCount = 0
  letterMap = {}

  while right < len(string):
    letterMap[string[right]] = letterMap.get(string[right], 0) + 1
    if letterMap[string[right]] == 1 and string[right] in characters:
      characterCount += 1
    
    while characterCount == len(characters) and left < right:
      minLength = min(minLength, right - left + 1)
      letterMap[string[left]] -= 1
      if letterMap[string[left]] == 0 and string[left] in characters:
        characterCount -= 1
      left += 1
      

    right += 1
  

  return minLength


print(solution("adddddbcbba", {'a','b','c'})) # should be 4
print(solution("abc", {'a','b','c'})) # should be 3
print(solution("abdddddcbeba", {'a', 'b', 'c'})) # should be 5
print(solution("abweweffawefcaaaaboiwuroqiwuroiueeeb", {'a', 'b', 'c'})) # should be 6