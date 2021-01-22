#BOJ 1000
A, B = map(int ,input().split())
print(A+B)

#BOJ 1001
A, B = map(int ,input().split())
print(A-B)

#BOJ 1008
A, B = map(int ,input().split())
print(A/B)

#BOJ 2557
print("Hello World!")

#BOJ 10171
print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")

#BOJ 10172
print("|\\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print("||_/=\\\\__|")

#BOJ 10869
A, B =map(int, input().split())
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)

#BOJ 10871
print("강한친구 대한육군\n강한친구 대한육군")

#BOJ 10998
A, B = map(int ,input().split())
print(A*B)

#BOJ 2588
data1 = int(input())
data2 = int(input())
print(data1+data2)

#BOJ 2558
data1 = int(input())
data2 = input()
list(data2)

for i in range(2,-1,-1):
    print(data1*int(data2[i]))

print(data1*int(data2))


#BOJ 3046
R1, S = map(int, input().split(" "))
print(2 * S - R1)

#BOJ 2163
N, M = map(int, input().split())
print(N*M -1)

#BOJ 11021
N = int(input())
for i in range(1, N+1):
    A, B = map(int, input().split(" "))
    print("Case #{0}: {1}".format(i, A+B))

#BOJ 11022
N = int(input())
for i in range(1, N+1):
    A, B = map(int, input().split(" "))
    print("Case #{0}: {1} + {2} = {3}".format(i, A, B, A+B))

#BOJ 10699
import time
seoul = time.strftime('%Y-%m-%d',time.localtime())
print(seoul)

#BOJ 2525
a, b = map(int, input().split(" "))
chicken = int(input())

if b + chicken >=60:
    a += (b+chicken)//60
    total = (b+chicken)%60

else:
    total = b+chicken

a%=24

print(a, total)


# BOJ 2530
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


#BOJ 2675

T = int(input())

for x in range(T):
    num,s = input().split(" ")
    text=""
    for i in s:
        text += int(num) * i

    print(text)

#BOJ 2935

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

# BOJ 9498
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

# BOJ 10817
a,b,c = map(int, input().split(" "))
list_answer = [a,b,c]
list_answer.sort(reverse=True)
print(list_answer[1])

# BOJ 11653
a = int(input())
result = []

while a !=1:
    for i in range(2, a+1):
        if a % i ==0:
            result.append(i)
            a = a//i
            break
for i in result:
    print(i)

# BOJ 1330
a, b = map(int,input().split(" "))

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    a == b
    print("==")

# BOJ 2753

a = int(input())

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("1")
else:
    print("0") 

# BOJ 14681

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
elif x > 0 and y < 0:
    print("4")

# BOJ 2884

a, b = map(int, input().split(" "))
if b > 44:
    print(a, b-45, sep=" ")
elif b < 45 and a > 0:
    print(a-1, b+15, sep=" ")

else:
    print(23, b+15)

# BOJ 10950

n = int(input())

for i in range (1, n+1):
    a, b = map(int, input().split(" "))
    print(a+b)

# BOJ 2739
n = int(input())

for i in range(1, 10):
    print("{} * {} = {}".format(n, i, n*i))

# BOJ 8393

n = int(input())
sum = 0
for i in range(1,n+1):
    sum += i

print(sum)

# BOJ 15552
import sys

a = int(sys.stdin.readline())
for i in range(1,a+1):
    x,y = map(int,sys.stdin.readline().split())
    print(x+y)

# BOJ 2741
N = int(input())

for i in range(1,N+1):
    print(i)

# BOJ 2742
N = int(input())

for i in range(N, 0, -1):
    print(i)

# BOJ 2438
n = int(input())

for i in range(1,n+1):
    print("*"*i)

# BOJ 2439

n = int(input())

for i in range(1,n+1):
    print(str("*"*i).rjust(n))

# BOJ 10871
import sys

n, m = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))

for num in a:
    if int(num) < m:
        print(int(num), end=" ")

# BOJ 10952
import sys

while  True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break

    print(n+m)

# BOJ 10951

import sys

while  True:
    try:
        n, m = map(int, sys.stdin.readline().split())
        print(n+m)
        
    except:
        break

# BOJ 10757
a, b = map(int,input().split())
print(a+b)

# BOJ 2480
a,b,c = map(int,input().split())

if a==b==c:
    print((a*1000)+10000)
elif a==b:
    print((a*100)+1000)
elif b==c:
    print((a*100)+1000)
elif a==c:
    print((a*100)+1000)
else:
    print(max(a,b,c)*100)

# BOJ 10156
k, n, m = map(int,input().split())

if m - (k*n) > 0:
    print(0)

elif m - (k*n) < 0:
    print((k*n)-m)

# BOJ 10162


t = int(input())

if not t % 10 == 0:
    print(-1)

else:
    a=0
    b=0
    c=0
    a = t // 300
    b = (t % 300) // 60
    c = (t % 300) % 60 // 10
    print(a, b, c)

# BOJ 10039
a = int(input())
b = int(input()) 
c = int(input())
d = int(input())
e = int(input())

if a < 40 :
    a = 40
if b < 40:
    b = 40
if c < 40:
    c = 40
if d < 40:
    d = 40
if e < 40:
    e = 40

print(int((a+b+c+d+e))//5)

# BOJ 10953
n = int(input())

for i in range (1, n+1):
    a, b = map(int, input().split(","))
    print(a+b)

# BOJ 2754
s = input()

if s == 'A+':
    print(4.3)
elif s == 'A0':
    print(4.0)
elif s == 'A-':
    print(3.7)
elif s == 'B+':
    print(3.3)
elif s == 'B0':
    print(3.0)
elif s == 'B-':
    print(2.7)
elif s == 'C+':
    print(2.3)
elif s == 'C0':
    print(2.0)
elif s == 'C-':
    print(1.7)
elif s == 'D+':
    print(1.3)
elif s == 'D0':
    print(1.0)
elif s == 'D-':
    print(0.7)
elif s == 'F':
    print(0.0) 

# BOJ 5063
n = int(input())
for i in range(1, n+1):
    r, e, c = map(int, input().split())
    if e - c > r:
        print("advertise")
    elif e - c - r == 0:
        print("does not matter")
    elif e - c < r:
        print("do not advertise")  

# BOJ 5717
while True:
    m, f = map(int,input().split())
    if m ==0 and f ==0:
        break
    else:
        print(m+f)

# BOJ 2476
n = int(input())
answer = 0
for i in range(n):
    x,y,z = map(int,input().split())
    if x == y ==z:
        answer = max(answer, 10000+(x*1000))
    elif x == y:
        answer = max(answer, 1000+(x*100))
    elif y == z:
        answer = max(answer, 1000+(y*100))
    elif x == z:
        answer = max(answer, 1000+(x*100))
    else:
        answer = max(answer, (max(x,y,z)*100))
   
print(answer)

# BOJ 10103
a = 100
b = 100
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    if x < y :
        a -= y
    elif x == y:
        a += 0
        b += 0
    elif x > y:
        b -= x

print(a)
print(b)

# BOJ 4101

while True:
    x, y = map(int,input().split())
    if x == 0 and y == 0:
        break
    elif x < y :
        print("No")
    elif x == y :
        print("No")
    elif x > y :
        print("Yes")

# BOJ 10886

n = int(input())
result = 0
for i in range(n):
    a = int(input())
    if a == 1:
        result += 1

    
if result > n //2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")

# BOJ 5086

while True:
    x, y = map(int,input().split())
    if x == 0 and y == 0:
        break

    elif y % x == 0:
        print("factor")
    
    elif x % y  == 0:
        print("multiple")

    else:
        print("neither")

# BOJ 3009
sq = []
x = []
y = []

for i in range(3):
    sq.append(list(map(int,input().split())))
for [a, b] in sq:
    if a in x:
        x.remove(a)
    else:
        x.append(a)
    
    if b in y:
        y.remove(b)
    else:
        y.append(b)

print(x[0], y[0])

# BOJ 9610

n = int(input())
Q1= Q2= Q3= Q4 = AXIS =0
for i in range(n):
    x, y = map(int,input().split())
    if x > 0 and y > 0:
        Q1 += 1
    elif x < 0 and y > 0:
        Q2 += 1
    elif x < 0 and y < 0:
        Q3 += 1
    elif x > 0 and y < 0:
        Q4 += 1
    else:
        AXIS += 1
print("Q1: {}".format(Q1))
print("Q2: {}".format(Q2))
print("Q3: {}".format(Q3))
print("Q4: {}".format(Q4))
print("AXIS: {}".format(AXIS))

# BOJ 10214

n = int(input())
for i in range(n):
    xcnt = ycnt = 0
    for j in range(9):
        x ,y = map(int,input().split())
        if x > 0:
            xcnt +=1
        elif y > 0:
            ycnt +=1

    if xcnt > ycnt:
        print("Yonsei")

    elif xcnt < ycnt:
        print("Korea")

    else:
        ("Draw")

# BOJ 10102

v = int(input())
o = list(str(input()))
acnt = 0
bcnt = 0
for i in o:
    if i == "A":
        acnt += 1

    elif i == "B":
        bcnt += 1

if acnt > bcnt:
    print("A")
elif acnt < bcnt:
    print("B")
else:
    print("Tie")

# BOJ 7567

d = list(str(input()))
h = 0
for i in range(len(d)):
    if i == 0:
        h += 10
    elif d[i] == d[i-1]:
        h += 5
    else:
        h += 10


print(h)

# BOJ 2440

n = int(input())

for i in range(n, 0, -1):
    print("*" * i)

# BOJ 2441

n = int(input())

for i in range(n, 0, -1):
    b = ("*" * i).rjust(n)
    print(b)

# BOJ 2442

n = int(input())
for i in range(1, n+1):
    result = " " * (n-i)+ "*" *(2*i-1)
    print(result)