#https://leetcode.com/problems/reverse-bits/
n = 4294967293
num = format(n ,'b') #get bit representation as a string
num = num.zfill(32) #make it 32 bit long
rev = num[::-1] #reverse num
# print(int(rev, 2)) #will give the number directly

#to get num from binary representation
ans = 0
exp = 1
for i in range(len(rev)-1, -1, -1):
    ans += int(rev[i])*exp
    exp = 2*exp
print(ans)

# #single line 
# print(int(format(n,'b').zfill(32)[::-1],2))
