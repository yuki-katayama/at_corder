#A
a = int(input())

print(2 * a * 3.14)


n , m = map(int, input().split())
a = list(map(int, input().split()))

print(max(n - sum(a), -1))


#B
n,m = map(int, input().split())
a = list(map(int, input().split()))

print(max(n - sum(a), - 1))

#C
import collections
n= int(input())
a = list(map(int, input().split()))

count = collections.Counter(a)
for i in range(n):
    print(count[i + 1])
