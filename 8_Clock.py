import datetime
import os
import time
from colorama import init
init()
from colorama import Fore, Back, Style


while True:
    current_date_time = datetime.datetime.now()
    current_time = current_date_time.time()
    out_time=current_time.strftime("%H:%M:%S")
    out_time_sec=current_time.strftime("%S")
    
    
    
    with open("numbers", "r", encoding="utf-8") as file_numbers:
        text = file_numbers.readlines()
        
        text_new=[]
        for i in text:
            i_new=i.replace("\n", "")
            text_new.append(i_new)

        for i in range(5):
            a=""
            for el in out_time:
                if el in "0123456789":
                    n=int(el)
                    a=a+text_new[n*5:(n+1)*5][i]+"     "
                else:
                    if int(out_time_sec)%2==0:
                        a=a+text_new[50:55][i]+"     "
                    else:
                        a=a+"     "+"     "
                    
            print(a)
        
        
    time.sleep(1)
    os.system('cls')

