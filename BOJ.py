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

#BOJ10699
import time
seoul = time.strftime('%Y-%m-%d',time.localtime())
print(seoul)

#BOJ2525
a, b = map(int, input().split(" "))
chicken = int(input())

if b + chicken >=60:
    a += (b+chicken)//60
    total = (b+chicken)%60

else:
    total = b+chicken

a%=24

print(a, total)


# BOJ2530
h, m, s = map(int, input().split(" "))
ds = int(input())

s += ds % 60
ds = ds//60
if s >= 60:
    s -= 60
    m += 1

m += ds % 60
ds = ds//60
if m >= 60:
    m -= 60
    h += 1

h += ds % 24
if h >= 24:
    h -= 24

print(h, m ,s)

#BOJ 2914
a, b = map(int,input().split(" "))
print((b-1)*a +1)   

#BOJ 5355
t = int(input())

for x in range(t):
    mars = list(map(str, input().split(" ")))
    answer = 0
    for i in range(len(mars)):
        if i == 0:
            answer += float(mars[i])
        else:
            if mars[i] =="#":
                answer -= 7
            elif mars[i] == "%":
                answer += 5
            elif mars[i] == "@":
                answer *= 3
    print("%.2f" % answer)


#BOJ2675

T = int(input())

for x in range(T):
    num,s = input().split(" ")
    text=""
    for i in s:
        text += int(num) * i

    print(text)

#BOJ2935

a = int(input())
a_1 = input()
b = int(input())
answer = 0
if a_1 == "+":
    answer += a+b
else:
    a_1 == "*"
    answer += a*b

print(answer)

# BOJ9498
a = int(input())
if 90 <= a <= 100:
    print("A")
elif 80<= a < 90:
    print("B")
elif 70 <= a < 80:
    print("C")
elif 60 <= a <70:
    print("D")
else:
    print("F")

# BOJ10817
a,b,c = map(int, input().split(" "))
list_answer = [a,b,c]
list_answer.sort(reverse=True)
print(list_answer[1])