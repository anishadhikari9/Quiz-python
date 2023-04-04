##defining the currency exchange rate and currency based on country

def convertSalary(salary, country):
 
    if country == "Canada":
        rate = 1
        currency = "CAD"
    elif country == "USA":
        rate = 1.18
        currency = "USD"
    elif country == "Cambodia":
        rate = 4847.38
        currency = "Cambodian riel"
    elif country == "United Kingdom":
        rate = 0.91
        currency = "Pound Sterling"
    else:
        #if country is invalid,print error message and return none
        
        print("Invalid country input.")
        return
    
#converting salary to new currency
    converted_salary = salary * rate
    return converted_salary, currency


salary = float(input("Enter your salary per annum in Euros: "))
country = input("Enter the country you want to migrate to: ")

result = convertSalary(salary, country) #(calling the function to convert salary and get the result)

if result:
    converted_salary, currency = result
    if country == "Canada":
        average_salary = 64000
    elif country == "USA":
        average_salary = 56516
    elif country == "Cambodia":
        average_salary = 5649856
    elif country == "United Kingdom":
        average_salary = 35423

#checking if the user's converted salary is greater than the average salary for the chosen particular country
    if converted_salary > average_salary:
        print(f"You will be rich in {country} with a salary of {converted_salary:.2f} {currency}")
    else:
        print(f"You will be poor in {country} with a salary of {converted_salary:.2f} {currency}")
