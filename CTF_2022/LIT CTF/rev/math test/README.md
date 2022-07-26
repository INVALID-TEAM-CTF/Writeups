# math test
Category: Reverse Engineering

Score: 131 (solved by 176 teams)

Original description: this math test is hard

# Introduction
У нас есть [программа](https://github.com/silver12-A/Writeups/blob/main/CTF_2022/LIT%20CTF/rev/math%20test/math), которая выводит строку `Добро пожаловать на тест по математике. Если вы получите идеальный результат, я распечатаю флаг!`.

# Analyzing IDA PRO
В `main()` задается вопрос и просит ввести результат:

```int __cdecl main(int argc, const char **argv, const char **envp)
{
  int i; // [rsp+Ch] [rbp-4h]

  puts("Welcome to the math test. If you get a perfect score, I will print the flag!");
  puts("All questions will have non-negative integer answers.\n");
  for ( i = 0; i < NUM_Q; ++i )
  {
    printf("Question #%d: ", (unsigned int)(i + 1));
    puts((&questions)[i]);
    __isoc99_scanf("%llu", &submitted[i]);
  }
  return grade_test();
}
```
Например:
![image](https://user-images.githubusercontent.com/55994705/180990331-af35757f-7d61-4a46-a899-51db647829f1.png)


# Solution script
Сценарий реализации решения можно найти [здесь](https://github.com/silver12-A/Writeups/blob/main/CTF_2022/BDSec_CTF_2022/Reverse%20Engineering/BDSec%20License%20Checker%200x1/solver.py).


flag is: BDSEC{1c3n53_ch3ck3r_0x1_2022}
