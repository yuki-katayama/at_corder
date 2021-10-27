#A
a ,b, c = map(int, input().split())
print(c,a,b)

#B
n, m=  map(int, input().split()) #n種類の中からm個選ぶ時
a = list(map(int, input().split())) #n種類の投票数  pythonではn使わなくてもいける

all_vote = sum(a)

cnt = 0
for a in a:
    if( 4 * m *a >= all_vote):
        cnt+=1
if cnt >= m:
    print("Yes")
else:
    print("No")

#C
#N>K →N%K < K
#N<K →N%K < K
#よって min(N%K, K-(N%K)) ←絶対値はこの二つを繰り返す
#Mがマイナスの時はK-Mで使う
n,k =map(int, input().split())
m = n % k
print(min(m, k - m))
