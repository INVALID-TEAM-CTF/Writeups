# not assembly
Category: Reverse Engineering

Score: 170 (solved by 173 teams)

Original description: Find the output and wrap it in LITCTF{} !

# Introduction
Нам дается картинка ![notassembly](https://user-images.githubusercontent.com/55994705/181242331-5c545d02-1dbe-450b-8e57-994800c5e97d.png)

Это обычный цикл

```flag=0
codetiger=23
orz=4138
while True:
   orz*=3
   orz+=codetiger
   flag=orz
   orz-=9538
   if orz<=0:
      break
flag-=3571
print(flag)```

flag is: BDSEC{5149}
