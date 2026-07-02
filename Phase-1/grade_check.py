#Getting input from user
marks = int(input("Enter your marks: "))

#Checking the grade
if marks >=90 and marks <= 100:
    print("Grade: A")
elif marks >= 75 and marks < 90:
    print("Grade: B")
elif marks >= 50 and marks < 75:
    print("Grade: C")
elif marks >100:
    print("Invalid marks. Please enter marks between 0 and 100.")
else:
    print("Grade: Fail")
