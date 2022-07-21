temp=[71,91,43,101,81,326,99,104,20,16,40,20,64,104,406,20,104,706,20,416,64,89,26,99,64,10,89,10,10,526]
index=0
for j in temp:
   for i in range(33,127):
      v3=0
      flag=i
      while flag:
         v3=10*v3+flag%10
         flag//=10
      if v3+5==j:
         print(chr(i),end='')