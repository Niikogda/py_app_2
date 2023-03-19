number=(int(input('введіть число: ')))
number_1=int(number/100)
number_2=int(number/10)%10
number_3=int(number%10)
print(number_1)
print(number_2)
print(number_3)
print(number_1+number_2+number_3)