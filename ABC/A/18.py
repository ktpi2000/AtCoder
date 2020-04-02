# 豆まき
a = input()
b = input()
c = input()

if c < a and c < b and b < a:
    print("1\n2\n3")
if c < a and c < b and b > a:
    print("2\n1\n3")
if a < b and a < c and b < c:
	print("3\n2\n1")
if a < b and a < c and b > c:
	print("3\n1\n2")
if b < a and b < c and a < c:
	print("2\n3\n1")
if b < a and b < c and a > c:
	print("1\n3\n2")
