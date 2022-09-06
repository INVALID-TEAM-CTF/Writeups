SOLVER 
See No Evil 1,2,3,4,5

Т.к. в `printf()`, при выводе адреса, передается указатель на строку, то можно пропатчить строчку

'''
.rdata:0000000140029898 Format          db 'Your flag is at 0x%016IX',0Ah,0

'''

на 

'''
.rdata:0000000140029898 Format          db 'Your flag is at   %s    ',0Ah,0

'''


тем самым получить всле флаги:

![image](https://user-images.githubusercontent.com/55994705/188719678-e3f0d2b3-45c6-4503-88ad-bb80fd60bfce.png)


`[*] Level 1... Your flag is at   FLAG-JDGIkhGvlCcoojXduitQuZKpGv`
`[*] Level 2... Your flag is at   FLAG-VMOkKL86JbTuhEViFvxyao4H2k`
`[*] Level 3... Your flag is at   FLAG-cjpG8FaodZgx2x3Prf6igbv7Zh`
`[*] Level 4... Your flag is at   FLAG-JzeQdOb0VNJsbDRGc2pwSNkffk`
`[*] Level 5... Your flag is at   FLAG-Ukow9CQfAZWBixEOIlZlrdtjZs`
