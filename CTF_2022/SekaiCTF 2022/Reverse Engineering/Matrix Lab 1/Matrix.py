from z3 import *

s = Solver()

def getArray(array,n,n2):
   array2=[]
   for i in range(6):
      array2.append(array[n][i])
   for j in range(6):
      array2.append(array[n2][6 - 1 - j])
   return array2
 
def encrypt(array,n):
   data=[]
   n2=5
   length=6
   for i in range(0,12,2):
      data.append(array[n2])
      n2-=1
      data.append(array[length])
      length+=1
   for i in range(12):
      array2=data
      array2[i]^=n
   return data
a = [BitVec(f'a{i}', 64) for i in range(36)]
transform=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]


for i in range(36):
    s.add(And(a[i] >= ord('!'), a[i] <= ord('}')))
for i in range(36):
   transform[i//6][i%6]=a[i]
for i in range(4):
   for j in  range(6-2*i-1):
      c=transform[i][i+j]
      transform[i][i + j] = transform[6 - 1 - i - j][i]
      transform[6 - 1 - i - j][i] = transform[6 - 1 - i][6 - 1 - i - j]
      transform[6 - 1 - i][6 - 1 - i - j] = transform[i + j][6 - 1 - i]
      transform[i + j][6 - 1 - i] = c
print(transform)
flag1=getArray(transform,0,5)
flag1=encrypt(flag1,2)
flag2=getArray(transform,1,4)
flag2=encrypt(flag2,1)
flag3=getArray(transform,2,3)
flag3=encrypt(flag3,0)

eq='oz]{R]3l]]B#'  
p=0
for i in eq:
    s.add(flag1[p]==ord(i))
    p+=1
eq2='50es6O4tL23E'
p=0
for i in eq2:
    s.add(flag2[p]==ord(i))
    p+=1
print(s.check())

eq3='tr3c10_F4TD2'
p=0
for i in eq3:
    s.add(flag3[p]==ord(i))
    p+=1
print(s.check())
m = s.model()
print(m)
flag = {}

for d in m.decls():
    flag[int(d.name()[1:])] = m[d].as_long()

w = ''

for i in sorted(flag):
    w += chr(flag[i])

print(w)