# Poster
Category: Reverse Engineering

Score: 100 (solved by 103 teams)

In Poster there is no string.

# Introduction
У нас есть [программа](https://github.com/silver12-A/Writeups/blob/main/CTF_2022/BDSec_CTF_2022/Reverse%20Engineering/Poster/poster), в которой по адресу `0x2960` храниться flag.

'''
.rodata:0000000000002938 ; const char s[]
.rodata:0000000000002938 s               db 'Congratulations password iss  your flag',0
.rodata:0000000000002938                                         ; DATA XREF: main+73↑o
.rodata:0000000000002960 aBdecThisStartY:                        ; DATA XREF: .data:flag↓o
.rodata:0000000000002960                 text "UTF-16LE", 'BDEC{this_Start_your_re_journey}'
.rodata:0000000000002960 _rodata         ends
.rodata:0000000000002960

'''

flag is: BDEC{this_Start_your_re_journey}
