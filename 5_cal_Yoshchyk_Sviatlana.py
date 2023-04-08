weight = float(input("Input weight: "))
height = float(input("Input height in meters: "))
body_mass_index = int(weight / (height ** 2))
print("Your body mass index: ", body_mass_index)
print("12" + (body_mass_index - 12) * "=" + "|" + (40 - body_mass_index) * "=" + "40")

age = int(input("Your age: "))
gender = input("Your gender: female or male?")
list_of_diagnoses = ["excessive exhaustion","underweight", "normal weight", "excess weight", "severe obesity"]
list_recommendation = [
"\nEat more calories! \nEat more often! \nDrink protein shakes!" ,
"\nEat more calories! \nGo in for sports! \nDrink protein shakes!", 
"\nGo in for sports! \nGet outdoors more! \nDon't forget to eat right!",
"\nGo in for sports! \nEat fewer calories! \nDinner is recommended no later than 3-4 hours before bedtime!", 
"\nGo in for sports! \nEat fewer calories! Eat foods high in protein \nDinner is recommended no later than 3-4 hours before bedtime!"
]

if gender == "female":
    if age < 8:
        print("Your body is still growing! It's too early to think about it! But the main thing is to eat right, walk in the fresh air and play sports!")
    elif age< 9:
        if body_mass_index < 12.4:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 13.2:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 15.9:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 18.8:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])
    elif age < 10:
        if body_mass_index < 12.9:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 13.4:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 16.4:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 19.7:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 11:
        if body_mass_index < 13.4:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 14.2:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 16.9:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 20.7:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 12:
        if body_mass_index < 13.8:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 14.6:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 17.7:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 20.8:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 13:
        if body_mass_index < 14.8:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 16.0:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 18.4:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 21.5:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 14:
        if body_mass_index < 15.2:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 15.6:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 18.9:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 22.1:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 15:
        if body_mass_index < 16.2:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 17.0:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 19.4:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 23.1:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 16:
        if body_mass_index < 16.9:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 17.6:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 20.2:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 23.3:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 17:
        if body_mass_index < 16.9:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 17.8:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 20.3:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 22.8:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 18:
        if body_mass_index < 17.2:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 17.9:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 20.5:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 23.3:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 24:
        if body_mass_index < 19:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 22:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 24:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 29:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 34:
        if body_mass_index < 20:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 22:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 25:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 30:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 44:
        if body_mass_index < 21:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 23:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 26:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 31:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 54:
        if body_mass_index < 22:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 24:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 27:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 32:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 64:
        if body_mass_index < 23:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 25:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 28:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 33:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    else:
        print("You have reached such an age that almost everything is possible for you. \n Do not forget: life is a framework, so walk in the fresh air, eat right.\n A healthy lifestyle is the key to success.")


if gender == "male":
    if age  < 8:
        print("Your body is still growing! It's too early to think about it! But the main thing is to eat right, walk in the fresh air and play sports!")
    elif age < 9:
        if body_mass_index < 12.5:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 14.2:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 16.4:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 19.3:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])
    elif age < 10:
        if body_mass_index < 12.8:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 13.8:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 17.1:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 19.5:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 11:
        if body_mass_index < 13.8:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 14.6:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 17.1:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 21.4:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 12:
        if body_mass_index < 14.2:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 14.3:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 17.8:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 21.2:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 13:
        if body_mass_index < 14.6:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 14.8:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 18.5:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 22.0:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 14:
        if body_mass_index < 15.6:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 16.2:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 19.1:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 21.7:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 15:
        if body_mass_index < 16.1:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 16.7:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 19.8:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 22.6:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 16:
        if body_mass_index < 17.1:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 17.8:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 20.2:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 23.1:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 17:
        if body_mass_index < 17.7:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 18.5:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 21.1:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 23.6:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 18:
        if body_mass_index < 17.5:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 18.5:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 21.6:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 23.7:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 24:
        if body_mass_index < 20:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 22:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 25:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 30:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 34:
        if body_mass_index < 21:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 23:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 26:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 31:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 44:
        if body_mass_index < 22:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 23:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 27:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 32:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 54:
        if body_mass_index < 23:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 25:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 28:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 33:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    elif age < 64:
        if body_mass_index < 24:
            print("Your the diagnoses:", list_of_diagnoses[0])
            print("Recommendations for you:", list_recommendation[0])
        elif body_mass_index < 26:
            print("Your the diagnoses:", list_of_diagnoses[1])
            print("Recommendations for you:", list_recommendation[1])
        elif body_mass_index < 29:
            print("Your the diagnoses:", list_of_diagnoses[2])
            print("Recommendations for you:", list_recommendation[2])
        elif body_mass_index < 34:
            print("Your the diagnoses:", list_of_diagnoses[3])
            print("Recommendations for you:", list_recommendation[3])
        else:
            print("Your the diagnoses:", list_of_diagnoses[4])
            print("Recommendations for you:", list_recommendation[4])

    else:
        print("You have reached such an age that almost everything is possible for you. \n Do not forget: life is a framework, so walk in the fresh air, eat right.\n A healthy lifestyle is the key to success.")
        