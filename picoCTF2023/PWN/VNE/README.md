# VNE #
Category: Binary Exploitation

 
Score: 200
 
 Original description: We've got a binary that can list directories as root, try it out !!
Additional details will be available after launching your challenge instance.
 
 
# Hints
Have you checked the content of the /root folder

Find a way to add more instructions to the ls

   
## Solution ##
 
Запускаем ./bin

![image](https://user-images.githubusercontent.com/55994705/229237903-690fdf93-1c48-45e0-bdd9-7ec1c3a69fa3.png)
Эта программа не будет работать, если вы не зададите переменную окружения `SECRET_DIR`.

![image](https://user-images.githubusercontent.com/55994705/229237987-1e4efd8f-fbb4-4fbe-97f1-c831ae57fd7c.png)
Поскольку эта программа, вероятно, имеет уязвимость при внедрении команды, установим переменную среды с помощью следующей команды:
![image](https://user-images.githubusercontent.com/55994705/229238127-87c208ac-5407-4bec-8492-c2d91bdbbb7e.png)
и получим флаг

picoCTF{Power_t0_man!pul4t3_3nv_1670f174}

