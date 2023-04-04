# asking input from users

month = int(input("Enter the month in the numeric form: "))
day = int(input("Enter the day in numeric form: "))
year = input("Enter the year as two numerical digits (for example: 98, 20, 21): ")

#check whether the month, day and year are valid or not;
if month < 1 or month > 12:
    print("Error: Invalid Month Input")
elif day < 1 or day > 31:
    print("Error: Invalid Day Input")
elif not year.isdigit() or len(year) != 2:
    print("Error: Invalid Year Input")
    
# if all inputs are valid

else:
 print(f"{month}/{day}/{year}: Success: Congratulations! you entered the correct date.")
 
 