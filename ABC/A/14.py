# けんしょう先生のお菓子配り
a = int(input())
b = int(input())

c = a % b

if c == 0:
    print(c)
else:
    print(b - a % b)
