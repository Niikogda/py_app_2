x=int(input("input your number:  "))
a=int(x/1000)
b=int(x/100)%10
c=int(x/10)%10
d=int(x%10)
y=int(a*b*c*d)
print(int(y))
print(int(a))
print(int(b))
print(int(c))
print(int(d))