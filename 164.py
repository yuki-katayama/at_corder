#A
s,w = map(int , input().split())
if(s > w):
    print("safe")
else:
    print("unsafe")

#B
taka_h, taka_a, aoki_h, aoki_a = map(int, input().split())
 
while True:
    aoki_h -=taka_a
    taka_h -= aoki_a
    if(aoki_h <=0):
        print("Yes")
        break
    elif(taka_h <= 0):
        print("No")
        break
        
#C
import collections
kind = 0
n = int(input())
List = [input() for _ in range(n)]
d = collections.Counter(List)

for i in d.keys():
    kind += 1
print(kind)
