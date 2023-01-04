import random
a = 1
b = 0
c = 50
while a<=20:
  d = random.randint(1,50)
  if d > b:
    b = d
  if d < c:
    c = d
  if d == c:
    print('Mensagem')
  a+=1
print(b)
print(c)