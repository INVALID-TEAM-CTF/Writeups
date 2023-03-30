# MSB #
Category: Forensics

 
Score: 200
 
 Original description: This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image...
Download the image [here](https://github.com/INVALID-TEAM-CTF/Writeups/blob/main/picoCTF2023/Forensics/MSB/Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.png)
 
This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image...
 
# Hints
What's causing the 'corruption' of the image?

# Introduction
The description and name of challenge suggests data may be hidden in the Most Significant Bit (MSB) of the RGB pixels values within the image.

Поиск в Google позволил найти инструмент python `sigBits.py, который может извлекать данные из LSB и MSB для анализа.
   
## Solution ##
 
python sigBits.py -t=msb Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png

picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_b5e03bc5}
