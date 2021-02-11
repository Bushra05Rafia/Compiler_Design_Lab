s = input('enter the full string: ')
s_sub =input('enter the character to match: ')
count = 0
for i in range(len(s)):
  if s[i:i+len(s_sub)] == s_sub:
    print(s[i:i+len(s_sub)])
    count +=1

print('no of sub_string: ', count)