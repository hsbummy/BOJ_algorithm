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