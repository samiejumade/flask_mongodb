# Grade Checker
score = input("Enter your score: ")
score = int(score)
if score >= 90 : grade = "A"
elif 80 <= score < 89 : grade = "B"
elif 70 <= score < 79 : grade = "C"
elif 60 <= score < 69 : grade = "D"
else : grade = "F"
print("Your grade is", grade)