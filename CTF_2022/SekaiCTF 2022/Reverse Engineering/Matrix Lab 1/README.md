# Matrix Lab 1
Category: Reverse Engineering

Score: 100

Original description: Welcome to the first lab of Course ML10001 from Sekai University! The Lab 1 assignment should be pretty easy...

# Introduction
У нас есть [файл.class](https://github.com/INVALID-TEAM-CTF/Writeups/blob/main/CTF_2022/SekaiCTF%202022/Reverse%20Engineering/Matrix%20Lab%201/Matrix_Lab_1.class).

.class относится к java. Воспользуемся онлайн [декомпилятором](http://www.javadecompilers.com/) и получим код:


```import java.util.Scanner;

public class Sekai
{
    private static int length;
    
    public static void main(final String[] array) {
        final Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the flag: ");
        final String next = scanner.next();
        if (next.length() != 43) {
            System.out.println("Oops, wrong flag!");
            return;
        }
        final String substring = next.substring(0, Sekai.length);
        final String substring2 = next.substring(Sekai.length, next.length() - 1);
        final String substring3 = next.substring(next.length() - 1);
        if (substring.equals("SEKAI{") && substring3.equals("}")) {
            assert substring2.length() == Sekai.length * Sekai.length;
            if (solve(substring2)) {
                System.out.println("Congratulations, you got the flag!");
            }
            else {
                System.out.println("Oops, wrong flag!");
            }
        }
        else {
            System.out.println("Oops, wrong flag!");
        }
    }
    
    public static String encrypt(final char[] array, final int n) {
        final char[] data = new char[Sekai.length * 2];
        int n2 = Sekai.length - 1;
        int length = Sekai.length;
        for (int i = 0; i < Sekai.length * 2; ++i, ++i) {
            data[i] = array[n2--];
            data[i + 1] = array[length++];
        }
        for (int j = 0; j < Sekai.length * 2; ++j) {
            final char[] array2 = data;
            final int n3 = j;
            array2[n3] ^= (char)n;
        }
        return String.valueOf(data);
    }
    
    public static char[] getArray(final char[][] array, final int n, final int n2) {
        final char[] array2 = new char[Sekai.length * 2];
        int n3 = 0;
        for (int i = 0; i < Sekai.length; ++i) {
            array2[n3] = array[n][i];
            ++n3;
        }
        for (int j = 0; j < Sekai.length; ++j) {
            array2[n3] = array[n2][Sekai.length - 1 - j];
            ++n3;
        }
        return array2;
    }
    
    public static char[][] transform(final char[] array, final int n) {
        final char[][] array2 = new char[n][n];
        for (int i = 0; i < n * n; ++i) {
            array2[i / n][i % n] = array[i];
        }
        return array2;
    }
    
    public static boolean solve(final String s) {
        final char[][] transform = transform(s.toCharArray(), Sekai.length);
        for (int i = 0; i <= Sekai.length / 2; ++i) {
            for (int j = 0; j < Sekai.length - 2 * i - 1; ++j) {
                final char c = transform[i][i + j];
                transform[i][i + j] = transform[Sekai.length - 1 - i - j][i];
                transform[Sekai.length - 1 - i - j][i] = transform[Sekai.length - 1 - i][Sekai.length - 1 - i - j];
                transform[Sekai.length - 1 - i][Sekai.length - 1 - i - j] = transform[i + j][Sekai.length - 1 - i];
                transform[i + j][Sekai.length - 1 - i] = c;
            }
        }
        return "oz]{R]3l]]B#50es6O4tL23Etr3c10_F4TD2".equals(invokedynamic(makeConcatWithConstants:(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;, encrypt(getArray(transform, 0, 5), 2), encrypt(getArray(transform, 1, 4), 1), encrypt(getArray(transform, 2, 3), 0)));
    }
    
    static {
        Sekai.length = (int)Math.pow(2.0, 3.0) - 2;
    }
}
```

# Анализ кода

1. Длинна строки=43;
2. Первые 6 символов="SEKAI{";
3. Последний символ="}";
4. Sekai.length=6(видим это в конце кода);
5. Переменная substring2 содержит строки, которые находяться между скобками {   }

# Solution script
Сценарий реализации решения можно найти [здесь](https://github.com/silver12-A/Writeups/blob/main/CTF_2022/BDSec_CTF_2022/Reverse%20Engineering/BDSec%20License%20Checker%200x1/solver.py).


flag is: BDSEC{1c3n53_ch3ck3r_0x1_2022}
