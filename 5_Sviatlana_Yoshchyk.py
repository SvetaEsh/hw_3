# create a sheet of 3 values 
list = []
for i_num in range(3):
    list.append(int(input(f"Input {i_num+1} number: ")))
    
#If there are no zeros, output "No zero values"
while list.count(0) < 1:
   print("No null values!!!!]")
   break

#Output the first non-zero value. If all zeros are entered, output "All zeros entered"
print("Output the first non-zero value. If all zeros are entered, output 'All zeros entered':", end=" ")
print(list[0] or list[1] or list[2] or "All zeros entered")

#If the first value is greater than the sum of the second and third, print a-b-c
#If the first value is less than the sum of the second and third, print b+c-a
if list[0] > (list[1] + list[2]):
    print("If the first value is greater than the sum of the second and third, print a-b-c:", list[0] - list[1] - list[2])
elif list[0] < (list[1] + list[2]):
    print("If the first value is less than the sum of the second and third, print b+c-a:", list[1] + list[2] - list[0])


#If the first value is greater than 50 and one of the remaining values ​​is greater than the first, print "Vasya"
if list[0] > 50 and (list[1] > list[0] or list[2] > list[0]):
    print("Vasya")
# If the first value is greater than 5 or both of the remaining values ​​are 7, output "Petya"
if list[0] > 5 or (list[1] == 7 and list[2] == 7):
    print("Petya")
















