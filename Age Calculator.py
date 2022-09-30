#1 Input the values
num_of_years = input("How many years do you want to live: ")
age = input("What is your current age? ")

#2 Type Conversion of string to integer
num_of_years = int(num_of_years)
age_as_int = int(age)

#3 Calculating Number of Years remaining
years_remaining = num_of_years - age_as_int

#4 Calculating Number of Years Months Days remaining
days_remaining = 365 * years_remaining
weeks_remaining = 52 * years_remaining
months_remaining = 12 * years_remaining

#5 Using f string we stored in a variable result
result = f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months"

#6 Output the result
print(result)