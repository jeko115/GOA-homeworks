# პროექტების სია  
projects = ["პროექტი 1", "პროექტი 2", "პროექტი 3", "პროექტი 4"]  
  
# შედეგის ბეჭდვა  
print(f"ჩემი პირველი პროექტი რაც გავაკეთე არის {projects[0]} და ჩემი ბოლო პროექტი კი არის {projects[-1]}.")  





# რიცხვების სია  
numbers = list(range(1, 11))  
  
# ორი ინდექსის არჩევა  
index1, index2 = 2, 7  # მაგალითისთვის, ინდექსები 2 და 7  
sum_of_indices = numbers[index1] + numbers[index2]  
print(f"რიცხვების {numbers[index1]} და {numbers[index2]} შეკრება არის {sum_of_indices}.")  






# რიცხვების სია  
numbers = list(range(1, 21))  
  
# ორი ინდექსის არჩევა  
index1, index2 = 5, 15  
  
# ჩამოთვლა 1 ინდექსიდან 2 ინდექსამდე  
for num in numbers[index1:index2+1]:  
    print(num)  







# რიცხვების სია  
numbers = list(range(1, 31))  
  
# ინდექსის არჩევა  
selected_index = 10  
  
while True:  
    user_input = int(input("შეიყვანეთ ინდექსი (1-30): "))  
  
    if user_input > 30:  
        print("Incorrect, You must enter a number from 1 to 30.")  
    elif user_input == selected_index:  
        print("You guessed the number!")  
        break  
    else:  
        print("Incorrect, Please try again.")  







# რიცხვების სია  
numbers = list(range(1, 11))  
  
# ორი ინდექსის არჩევა  
index1, index2 = 3, 5  
  
product_of_indices = numbers[index1] * numbers[index2]  
print(f"რიცხვების {numbers[index1]} და {numbers[index2]} ნამრავლი არის {product_of_indices}.")  
