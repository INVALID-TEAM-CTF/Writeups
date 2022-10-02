# Matrix Lab 1
Category: Reverse Engineering

Score: 100

Original description: Welcome to the first lab of Course ML10001 from Sekai University! The Lab 1 assignment should be pretty easy...

# Introduction
У нас есть [файл.class](https://github.com/silver12-A/Writeups/blob/main/CTF_2022/BDSec_CTF_2022/Reverse%20Engineering/BDSec%20License%20Checker%200x1/bdsec_license_checker_1.out), которая запрашивает ввод лицензии.

# Analyzing IDA PRO
Анализ приводит к функции `ns_2(const char *a1)` где необходимо пройти условия:

```int __fastcall ns_2(const char *a1)
{
  int result; // eax
  int v2; // [rsp+14h] [rbp-ACh]
  int i; // [rsp+18h] [rbp-A8h]
  int v4[34]; // [rsp+20h] [rbp-A0h]
  unsigned __int64 v5; // [rsp+A8h] [rbp-18h]

  v5 = __readfsqword(0x28u);
  if ( strlen(a1) > 0x1F || strlen(a1) <= 0x1E )
    return puts("Invalid license key. Please try again.");
  v4[0] = 71;
  v4[1] = 91;
  v4[2] = 43;
  v4[3] = 101;
  v4[4] = 81;
  v4[5] = 326;
  v4[6] = 806;
  v4[7] = 99;
  v4[8] = 104;
  v4[9] = 20;
  v4[10] = 16;
  v4[11] = 40;
  v4[12] = 20;
  v4[13] = 64;
  v4[14] = 104;
  v4[15] = 406;
  v4[16] = 20;
  v4[17] = 104;
  v4[18] = 706;
  v4[19] = 20;
  v4[20] = 416;
  v4[21] = 64;
  v4[22] = 89;
  v4[23] = 26;
  v4[24] = 99;
  v4[25] = 64;
  v4[26] = 10;
  v4[27] = 89;
  v4[28] = 10;
  v4[29] = 10;
  v4[30] = 526;
  v2 = 0;
  for ( i = 0; i < strlen(a1); ++i )
  {
    if ( (unsigned int)ns_1((unsigned int)a1[i]) + 5 != v4[i] )
    {
      v2 = 0;
      break;
    }
    v2 = 1;
  }
  if ( v2 == 1 )
    result = puts("Congrats ! You found the right license key.");
  else
    result = puts("Invalid license key. Please try again.");
  return result;
}
```

# Solution script
Сценарий реализации решения можно найти [здесь](https://github.com/silver12-A/Writeups/blob/main/CTF_2022/BDSec_CTF_2022/Reverse%20Engineering/BDSec%20License%20Checker%200x1/solver.py).


flag is: BDSEC{1c3n53_ch3ck3r_0x1_2022}
