#BOJ1000
A, B = map(int ,input().split())
print(A+B)

#BOJ1001
A, B = map(int ,input().split())
print(A-B)

#BOJ1008
A, B = map(int ,input().split())
print(A/B)

#BOJ2557
print("Hello World!")

#BOJ10171
print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")

#BOJ10172
print("|\\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print("||_/=\\\\__|")

#BOJ10869
A, B =map(int, input().split())
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)

#BOJ10871
print("강한친구 대한육군\n강한친구 대한육군")

#BOJ10998
A, B = map(int ,input().split())
print(A*B)

#BOJ2588
data1 = int(input())
data2 = int(input())
print(data1+data2)

#BOJ2558
data1 = int(input())
data2 = input()
list(data2)

for i in range(2,-1,-1):
    print(data1*int(data2[i]))

print(data1*int(data2))


#BOJ3046
R1, S = map(int, input().split(" "))
print(2 * S - R1)

#BOJ2163
N, M = map(int, input().split())
print(N*M -1)

#BOJ11021
N = int(input())
for i in range(1, N+1):
    A, B = map(int, input().split(" "))
    print("Case #{0}: {1}".format(i, A+B))

#BOJ11022
N = int(input())
for i in range(1, N+1):
    A, B = map(int, input().split(" "))
    print("Case #{0}: {1} + {2} = {3}".format(i, A, B, A+B))