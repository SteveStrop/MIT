s = 'azcbobobegghakl'
print(f"Number of vowels: {sum([s.count(vowel) for vowel in 'aeiou'])}")
count=0
for letter in range(0,len(s)-2):
    if s[letter:letter+3]=='bob':
        count+=1
print(f'Number of times bob occurs is:{count}')
