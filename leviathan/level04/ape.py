s = "01010100 01101001 01110100 01101000 00110100 01100011 01101111 01101011 01100101 01101001 00001010"
s1 = s.split(' ')
ans = []
for i in s1:
    x=int(i,2)
    ans.append(chr(x))
print("".join(ans))
