#A
k = int(input())
a, b = map(int, input().split())
#A%k はkがAの倍数で、aとbの差がk無い時に役たつ
#a//k != b//k はaとbの間にkの倍数が入っているか見る
if(a % k == 0 or a//k != b//k):

    print("OK")
else:
    print("NG")

#B
x = int(input())
depo = 100
year = 0
while depo < x:
        depo += int(depo * 0.01)
        year += 1
print(year)

#C
#n+mCnの重複有組み合わせで全探索する
#後は条件を満たすような組み合わせを探せば良い
import itertools
n,m,q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(q)]
ans = 0
list_ = list(itertools.combinations_with_replacement(range(1, m + 1), n))
for i in list_:
    tmp = 0
    for a,b,c,d in arr:
        if (i[b-1] - i[a-1]==c):
            tmp+=d
    ans=max(ans,tmp)
print(ans)

#D
#小数部分の違いで考える
#x がb-1の時が最大になる
#しかしb-1がNより大きかった場合
#x=Nの時が最大である
def f(x):
    return a*x//b - a*(x//b)

a, b, n = map(int, input().split())

if b - 1 <= n:
    print(f(b-1))
else:
    print(f(n))
