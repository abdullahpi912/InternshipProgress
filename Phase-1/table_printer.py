#Getting input from user
number = int(input("Enter your number to get table for: "))

#Table printing logic
while True:
    for i in range(1, 11):
         print(f"{i} x {number} = {i * number}")
    str = input("Do you want to print another table? (y/stop): ")
    if str.lower() == "stop":
        break
