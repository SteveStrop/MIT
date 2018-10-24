s = 'abcdefghijklmnopqrstuvwxyz'
#s = 'zyxwvutsrqponmlkjihgfedcba'
#s = 'krnikovlazwdqikxlo'

a = a_max = s[0]
for i in range(1,len(s)):
    if s[i] >= s[i-1]:
        a += (s[i])
    else:
        a = s[i]
    if len(a) > len(a_max):
        a_max = a
print('Longest substring in alphabetical order is:', a_max)
