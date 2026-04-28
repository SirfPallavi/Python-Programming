import re
text = "hello world"
# result = re.match("hello", text)
# print(result)   # Match object
# result = re.match("world", text)
# print(result)   # None

result = re.search("world", text)
print(result)


text = "cat bat rat"
result = re.findall("at", text)
print(result)   # ['at', 'at', 'at']


text = "I like apples"
result = re.sub("apples", "mangoes", text)
print(result)


text = "I like apples"
result = re.sub("apples", "mangoes", text)
print(result)

