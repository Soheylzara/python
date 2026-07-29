# Task 1
print("Game Over")
# Task 2
num = 15
print(f"number : {num}")
mid_term = 19
final_exam = 37
sum = mid_term + final_exam
print(f"Sum of midterm and final exam {mid_term} + {final_exam} = {sum}")
# Task 3
age = int(input("enter age: "))
if age < 10:
    print("age : kid")
elif 10 <= age < 18:
    print("age : teenager")
elif 18 <= age < 40:
    print("age : adult")
else:
    print("age : elder")

Mid = int(input("Enter midterm: "))
Final = int(input("Enter final: "))
avg = (Mid + Final) / 2
print(f"Averange scores is : {avg}")
