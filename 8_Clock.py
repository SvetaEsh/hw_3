import datetime
import os
import time

"""

current_date_time = datetime.datetime.now()
current_time = current_date_time.time()
out_time=current_time.strftime("%H%M%S")
with open("numbers", "r", encoding="utf-8") as file_numbers:
        text = file_numbers.readlines()
        
        text_new=[]
        for i in text:
            i_new=i.replace("\n", "")
            
            text_new.append(i_new)

        print(text)
        print()
        print(text_new)
        

        for i in range(5):
            a=""
            for el in out_time:
                n=int(el)
                a=a+text_new[n*5:(n+1)*5][i]+"     "
            print(a)
"""



while True:
    current_date_time = datetime.datetime.now()
    current_time = current_date_time.time()
    out_time=current_time.strftime("%H%M%S")
    
    
    
    
    with open("numbers", "r", encoding="utf-8") as file_numbers:
        text = file_numbers.readlines()
        
        text_new=[]
        for i in text:
            i_new=i.replace("\n", "")
            text_new.append(i_new)

        for i in range(5):
            a=""
            for el in out_time:
                n=int(el)
                a=a+text_new[n*5:(n+1)*5][i]+"     "
            print(a)
        
        
    time.sleep(1)
    os.system('cls')

