# VNE #
Category: Binary Exploitation

 
Score: 200
 
 Original description: We've got a binary that can list directories as root, try it out !!
Additional details will be available after launching your challenge instance.
 
 
# Hints
Have you checked the content of the /root folder

Find a way to add more instructions to the ls

# Introduction

Поиск в Google позволил найти инструмент python `sigBits.py, который может извлекать данные из LSB и MSB для анализа.
   
## Solution ##
 
python sigBits.py -t=msb Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png

picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_b5e03bc5}

