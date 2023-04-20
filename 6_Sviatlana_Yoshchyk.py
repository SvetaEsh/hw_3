# for clear screen
import os

# init vocabulary
data_cal_bme = {1:
                {"Petya":
                 {"height": 1.62,
                  "weight": 75,
                  "gender": "male",
                  "age": 30}}, 
                2: 
                {"Vasya":
                 {"height": 1.82,
                  "weight": 75,
                  "gender": "male",
                  "age": 28}},
                3:
                {"Max":
                 {"height": 1.64,
                  "weight": 69,
                  "gender": "female",
                  "age": 34}}
                  }

# function for calc BME
# return string with BME scale
def cal_bme(height, weight):
    body_mass_index = int(weight / (height ** 2))
    shkala = "12" + (body_mass_index - 12) * "=" + "|" + (40 - body_mass_index) * "=" + "40"
    return shkala

# output list of all names in vocabulary
def list_name():
    for i_key in data_cal_bme.values():
            for key in i_key.keys():
                print(f"{key}")

# for return sub-vocabulary with given user 
def find_name(struct, key):
    if key in struct:
        return struct[key]
    for el_struct in struct.values():
        if isinstance(el_struct, dict):
            result=find_name(el_struct, key)
            if result:
                break
    else:
        result = None
    return result
        
while True:
# clear screen    
    os.system('cls')
    print("Menu")
    print("\n1. Display a list of users \n2. View user information \n3. Change user details \n4. Delete selected user \n5. Add user \n6. Exit")
    answer = int(input("Choose an action: "))
    os.system('cls')
    if  answer == 1:
        print("List of users: ")
        print( )
        list_name()        

    elif  answer == 2:
        print("List of users: ")
        print( )
        list_name()
        answre_info_name = input("Who do you need information about? Enter name: ")
        os.system('cls')
        list_data = find_name(data_cal_bme, answre_info_name)
        if list_data:
            height_name = list_data["height"]
            weight_name = list_data["weight"]   
            print("Info about", answre_info_name)   
            print("height:", height_name)
            print("weight:", weight_name)            
            print(cal_bme(height_name, weight_name))   

        else:
            print("There is no such person")

    elif  answer == 3:
        print("List of users: ")
        print( )
        list_name()
        answer_name = input("Which user do you want to change information about? ")
        os.system('cls')
        print(f"What information about {answer_name} would you like to change?") 
        print("1. Height \n2. Weight \n3. Gender \n4. Age")
        choice = int(input("Make a choice: "))
        os.system('cls')
        list_data = find_name(data_cal_bme, answer_name)
        if list_data:
            if choice == 1:
                new_height = float(input("Enter his height: "))
                find_name(data_cal_bme, answer_name)["height"] = new_height
                print(data_cal_bme)
            elif choice == 2:
                new_weight=int(input("Enter his weight: "))
                find_name(data_cal_bme, answer_name)["weight"] = new_weight
                print(data_cal_bme)
            elif choice == 3:
                new_gender=input("Enter his gender (female or male): ")
                find_name(data_cal_bme, answer_name)["gender"] = new_gender
                print(data_cal_bme)
            elif choice == 4:
                new_age= int(input("Enter his age: "))
                find_name(data_cal_bme, answer_name)["age"] = new_age
                print(data_cal_bme)
        else:
            print("There is no such person")
            
    elif  answer == 4:
        print("List of users: ")
        list_name()
        answre_info_name = input("Which user do you want to remove? ")
        list_data = find_name(data_cal_bme, answre_info_name)
        if list_data:
            i=1
            for el_dic in data_cal_bme.values():
                if answre_info_name in el_dic.keys():
                    i_index = i
                i += 1
        
            del data_cal_bme[i_index]
            print(data_cal_bme)
        else:
            print("There is no such person")    

    elif  answer == 5:
        nomer_next_key=list(data_cal_bme.keys())[-1]
        new_name = input("Enter a new username: ")
        new_height = float(input("Enter his height: "))
        new_weight = float(input("Enter his weight: "))
        new_gender = input("Enter his gender (female or male): ")
        new_age = int(input("Enter his age: "))
        data_cal_bme[nomer_next_key+1] = {new_name:{"height": new_height, "weight": new_weight, "gender": new_gender, "age": new_age}}
        print(data_cal_bme)

    elif answer == 6:
        print("Program finished")
        break

    input("Press Enter for continue...")



        
   
           
    
                       
                       

    

