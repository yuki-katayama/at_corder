#A--
S = input()
print("Yes" if S.count("7") else "No")


#B--
a = int(input())
ans = 0

for i in range(a+1):
    if(i % 3 != 0 and i % 5 != 0):
        ans += i
print(ans)


#C--
from math import gcd

K = int(input())

result = 0
for a in range(1, K + 1):
    for b in range(1, K + 1):
        t = gcd(a, b)
        for c in range(1, K + 1):
            result += gcd(t, c)
print(result)


#D--
n=int(input())
s=list(input())
ans=s.count('R')*s.count('G')*s.count('B') #1番目の条件を満たすものの総数は(Rの個数)*(Gの個数)*(Bの個数)
for i in range(n): #判定を簡単にするためR:=1,G:=2,B:=4と置き換えておく (i<j<K)
    if s[i]=='R':
        s[i]=1
    elif s[i]=='G':
        s[i] = 2
    elif s[i]=='B':
        s[i]=4
for i in range(n): #すべての(i,j) (i<j)について(i,j,2*j-i)が1番目の条件を満たし、かつ2番目の条件を満たさないかを判定する
    for j in range(i+1,n):
        k=2*j-i
        if k>=n: #k>=nのとき、そのような組を取ることはできない
            continue
        if s[i]+s[j]+s[k]==7: #i番目の数とj番目の数とk番目の数の和が7になるとき、(i,j,2*j-i)は1番目の条件を満たし、かつ2番目の条件を満たさないので、1番目の条件を満たすものの総数から1を引く
            ans-=1
print(ans)
