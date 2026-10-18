# WORKING WITH NUMBERS AND BOOLEANS IN PYTHON
"""
Name: Jose Valentin Alvarez Reyes
Tuition: 2630144
Group: 3
"""

# EXECUTIVE SUMMARY
"""
int is used for whole numbers.
float is used for decimal numbers.
bool has two values: True and False.
Comparisons create boolean values.
Arithmetic operators perform calculations.
and checks if all conditions are true.
or checks if at least one condition is true.
if allows the program to make decisions.
"""

# GOOD PRACTICES
"""
Use int for whole numbers.
Use float for decimal numbers.
Use clear variable names.
Check values before doing calculations.
Avoid division by zero.
"""


"""
PROBLEM 1: TEMPERATURE CONVERTER
Description: Convert Celsius to Fahrenheit and Kelvin.
Inputs: temp_c.
Outputs: Fahrenheit, Kelvin, and High temperature.
Validations: Temperature must be a number and Kelvin cannot be negative.
Tests: Normal: 25, Border: -273.15, Error: "hello".
"""

print("PROBLEM 1: TEMPERATURE CONVERTER")

temp_text = input("Enter temperature in Celsius: ")

try:
    temp_c = float(temp_text)

    temp_f = temp_c * 9 / 5 + 32
    temp_k = temp_c + 273.15

    if temp_k < 0:
        print("Error: invalid input")

    if temp_k >= 0:
        is_high_temperature = temp_c >= 30

        print("Fahrenheit:", round(temp_f, 2))
        print("Kelvin:", round(temp_k, 2))
        print("High temperature:", str(is_high_temperature).lower())

except ValueError:
    print("Error: invalid input")


"""
PROBLEM 2: WORK HOURS AND OVERTIME
Description: Calculate weekly payment and overtime.
Inputs: hours_worked and hourly_rate.
Outputs: Regular pay, overtime pay, total pay, and Has overtime.
Validations: Hours must be >= 0 and rate must be > 0.
Tests: Normal: 38, 100; Border: 40, 100; Error: -2, 100.
"""

print("\nPROBLEM 2: WORK HOURS AND OVERTIME")

try:
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")

    if hours_worked >= 0 and hourly_rate > 0:
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay

        has_overtime = hours_worked > 40

        print("Regular pay:", round(regular_pay, 2))
        print("Overtime pay:", round(overtime_pay, 2))
        print("Total pay:", round(total_pay, 2))
        print("Has overtime:", str(has_overtime).lower())

except ValueError:
    print("Error: invalid input")


"""
PROBLEM 3: DISCOUNT ELIGIBILITY
Description: Check if a customer can receive a 10% discount.
Inputs: purchase_total, is_student_text, and is_senior_text.
Outputs: Discount eligible and final total.
Validations: Purchase cannot be negative; answers must be YES or NO.
Tests: Normal: 500, YES, NO; Border: 1000, NO, NO; Error: -10, YES, NO.
"""

print("\nPROBLEM 3: DISCOUNT ELIGIBILITY")

try:
    purchase_total = float(input("Enter purchase total: "))
    is_student_text = input("Are you a student? YES/NO: ").upper()
    is_senior_text = input("Are you a senior? YES/NO: ").upper()

    if purchase_total < 0:
        print("Error: invalid input")

    if (purchase_total >= 0 and
        (is_student_text == "YES" or is_student_text == "NO") and
        (is_senior_text == "YES" or is_senior_text == "NO")):

        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"

        discount_eligible = (
            is_student or is_senior or purchase_total >= 1000
        )

        if discount_eligible == True:
            final_total = purchase_total * 0.9

        if discount_eligible == False:
            final_total = purchase_total

        print("Discount eligible:", str(discount_eligible).lower())
        print("Final total:", round(final_total, 2))

    if (is_student_text != "YES" and is_student_text != "NO") or \
       (is_senior_text != "YES" and is_senior_text != "NO"):
        print("Error: invalid input")

except ValueError:
    print("Error: invalid input")


"""
PROBLEM 4: STATISTICS OF THREE INTEGERS
Description: Calculate sum, average, maximum, minimum, and check if all are even.
Inputs: n1, n2, and n3.
Outputs: Sum, average, max, min, and All even.
Validations: Inputs must be integers.
Tests: Normal: 2, 4, 6; Border: 0, 0, 0; Error: 2, "hello", 6.
"""

print("\nPROBLEM 4: STATISTICS OF THREE INTEGERS")

try:
    n1 = int(input("Enter first integer: "))
    n2 = int(input("Enter second integer: "))
    n3 = int(input("Enter third integer: "))

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3

    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)

    all_even = n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0

    print("Sum:", sum_value)
    print("Average:", round(average_value, 2))
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", str(all_even).lower())

except ValueError:
    print("Error: invalid input")


"""
PROBLEM 5: LOAN ELIGIBILITY
Description: Check if a person qualifies for a loan.
Inputs: monthly_income, monthly_debt, and credit_score.
Outputs: Debt ratio and Eligible.
Validations: Income must be > 0; debt and score cannot be negative.
Tests: Normal: 10000, 2000, 700; Border: 8000, 3200, 650; Error: 0, 200, 700.
"""

print("\nPROBLEM 5: LOAN ELIGIBILITY")

try:
    monthly_income = float(input("Enter monthly income: "))
    monthly_debt = float(input("Enter monthly debt: "))
    credit_score = int(input("Enter credit score: "))

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")

    if monthly_income > 0 and monthly_debt >= 0 and credit_score >= 0:
        debt_ratio = monthly_debt / monthly_income

        eligible = (
            monthly_income >= 8000 and
            debt_ratio <= 0.4 and
            credit_score >= 650
        )

        print("Debt ratio:", round(debt_ratio, 2))
        print("Eligible:", str(eligible).lower())

except ValueError:
    print("Error: invalid input")


"""
PROBLEM 6: BMI CALCULATOR
Description: Calculate BMI and show its category flags.
Inputs: weight_kg and height_m.
Outputs: BMI, Underweight, Normal, and Overweight.
Validations: Weight and height must be > 0.
Tests: Normal: 70, 1.75; Border: 60, 2; Error: 0, 1.7.
"""

print("\nPROBLEM 6: BMI CALCULATOR")

try:
    weight_kg = float(input("Enter weight in kilograms: "))
    height_m = float(input("Enter height in meters: "))

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")

    if weight_kg > 0 and height_m > 0:
        bmi = weight_kg / (height_m * height_m)

        is_underweight = bmi < 18.5
        is_normal = bmi >= 18.5 and bmi < 25
        is_overweight = bmi >= 25

        print("BMI:", round(bmi, 2))
        print("Underweight:", str(is_underweight).lower())
        print("Normal:", str(is_normal).lower())
        print("Overweight:", str(is_overweight).lower())


except ValueError:
    print("Error: invalid input")


# CONCLUSIONS
"""
int is used for whole numbers and float for decimal numbers.
Comparisons create True or False values.
if helps the program make decisions.
and checks if all conditions are true.
or checks if at least one condition is true.
Input validation helps prevent incorrect calculations.
"""

# REFERENCES
"""
1. Python Documentation. Tipos integrados.
https://docs.python.org/es/3/library/stdtypes.html

2. Python Documentation. Tutorial de Python.
https://docs.python.org/es/3/tutorial/

3. Python Documentation. Funciones incorporadas.
https://docs.python.org/es/3/library/functions.html

4. Python Documentation. Introducción a Python.
https://docs.python.org/es/3/tutorial/introduction.html

5. Python Documentation. Errores y excepciones.
https://docs.python.org/es/3/tutorial/errors.html
"""