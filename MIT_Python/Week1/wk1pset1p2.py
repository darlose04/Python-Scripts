# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl'

count = 0
s = 'azcbobobegghakl'
pattern = 'bob'


for x in range(len(s) - 2):
    if s[x:x+len(pattern)] == pattern:
        count += 1
print('Number of times bob occurs is: {}'.format(count))
