# MANEJO DE NÚMEROS Y BOOLEANOS EN PYTHON
"""
Nombre: Jose Valentin Alvarez Reyes
Matrícula: 2630144
Grupo: 3
"""

# RESUMEN EJECUTIVO
"""
int se usa para números enteros.
float se usa para números decimales.
bool tiene dos valores: True y False.
Las comparaciones crean valores booleanos.
Los operadores aritméticos realizan cálculos.
and verifica si todas las condiciones son verdaderas.
or verifica si al menos una condición es verdadera.
if permite que el programa tome decisiones.
"""

# BUENAS PRÁCTICAS
"""
Usar int para números enteros.
Usar float para números decimales.
Usar nombres de variables claros.
Verificar los valores antes de hacer cálculos.
Evitar la división entre cero.
"""


"""
PROBLEMA 1: CONVERTIDOR DE TEMPERATURA
Descripción: Convertir Celsius a Fahrenheit y Kelvin.
Entradas: temp_c.
Salidas: Fahrenheit, Kelvin y temperatura alta.
Validaciones: La temperatura debe ser un número y Kelvin no puede ser negativo.
Pruebas: Normal: 25, Límite: -273.15, Error: "hello".
"""

print("PROBLEMA 1: CONVERTIDOR DE TEMPERATURA")

temp_text = input("Ingresa la temperatura en Celsius: ")

try:
    temp_c = float(temp_text)

    temp_f = temp_c * 9 / 5 + 32
    temp_k = temp_c + 273.15

    if temp_k < 0:
        print("Error: entrada inválida")

    if temp_k >= 0:
        is_high_temperature = temp_c >= 30

        print("Fahrenheit:", round(temp_f, 2))
        print("Kelvin:", round(temp_k, 2))
        print("Temperatura alta:", str(is_high_temperature).lower())

except ValueError:
    print("Error: entrada inválida")


"""
PROBLEMA 2: HORAS DE TRABAJO Y HORAS EXTRA
Descripción: Calcular el pago semanal y las horas extra.
Entradas: hours_worked y hourly_rate.
Salidas: Pago regular, pago de horas extra, pago total y tiene horas extra.
Validaciones: Las horas deben ser >= 0 y la tarifa debe ser > 0.
Pruebas: Normal: 38, 100; Límite: 40, 100; Error: -2, 100.
"""

print("\nPROBLEMA 2: HORAS DE TRABAJO Y HORAS EXTRA")

try:
    hours_worked = float(input("Ingresa las horas trabajadas: "))
    hourly_rate = float(input("Ingresa la tarifa por hora: "))

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: entrada inválida")

    if hours_worked >= 0 and hourly_rate > 0:
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay

        has_overtime = hours_worked > 40

        print("Pago regular:", round(regular_pay, 2))
        print("Pago de horas extra:", round(overtime_pay, 2))
        print("Pago total:", round(total_pay, 2))
        print("Tiene horas extra:", str(has_overtime).lower())

except ValueError:
    print("Error: entrada inválida")


"""
PROBLEMA 3: ELEGIBILIDAD PARA DESCUENTO
Descripción: Verificar si un cliente puede recibir un descuento del 10%.
Entradas: purchase_total, is_student_text e is_senior_text.
Salidas: Elegible para descuento y total final.
Validaciones: La compra no puede ser negativa; las respuestas deben ser YES o NO.
Pruebas: Normal: 500, YES, NO; Límite: 1000, NO, NO; Error: -10, YES, NO.
"""

print("\nPROBLEMA 3: ELEGIBILIDAD PARA DESCUENTO")

try:
    purchase_total = float(input("Ingresa el total de la compra: "))
    is_student_text = input("¿Eres estudiante? YES/NO: ").upper()
    is_senior_text = input("¿Eres adulto mayor? YES/NO: ").upper()

    if purchase_total < 0:
        print("Error: entrada inválida")

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

        print("Elegible para descuento:", str(discount_eligible).lower())
        print("Total final:", round(final_total, 2))

    if (is_student_text != "YES" and is_student_text != "NO") or \
       (is_senior_text != "YES" and is_senior_text != "NO"):
        print("Error: entrada inválida")

except ValueError:
    print("Error: entrada inválida")


"""
PROBLEMA 4: ESTADÍSTICAS DE TRES ENTEROS
Descripción: Calcular suma, promedio, máximo, mínimo y verificar si todos son pares.
Entradas: n1, n2 y n3.
Salidas: Suma, promedio, máximo, mínimo y todos pares.
Validaciones: Las entradas deben ser enteros.
Pruebas: Normal: 2, 4, 6; Límite: 0, 0, 0; Error: 2, "hello", 6.
"""

print("\nPROBLEMA 4: ESTADÍSTICAS DE TRES ENTEROS")

try:
    n1 = int(input("Ingresa el primer entero: "))
    n2 = int(input("Ingresa el segundo entero: "))
    n3 = int(input("Ingresa el tercer entero: "))

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3

    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)

    all_even = n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0

    print("Suma:", sum_value)
    print("Promedio:", round(average_value, 2))
    print("Máximo:", max_value)
    print("Mínimo:", min_value)
    print("Todos pares:", str(all_even).lower())

except ValueError:
    print("Error: entrada inválida")


"""
PROBLEMA 5: ELEGIBILIDAD PARA PRÉSTAMO
Descripción: Verificar si una persona califica para un préstamo.
Entradas: monthly_income, monthly_debt y credit_score.
Salidas: Ratio de deuda y elegible.
Validaciones: El ingreso debe ser > 0; la deuda y el puntaje no pueden ser negativos.
Pruebas: Normal: 10000, 2000, 700; Límite: 8000, 3200, 650; Error: 0, 200, 700.
"""

print("\nPROBLEMA 5: ELEGIBILIDAD PARA PRÉSTAMO")

try:
    monthly_income = float(input("Ingresa el ingreso mensual: "))
    monthly_debt = float(input("Ingresa la deuda mensual: "))
    credit_score = int(input("Ingresa el puntaje crediticio: "))

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: entrada inválida")

    if monthly_income > 0 and monthly_debt >= 0 and credit_score >= 0:
        debt_ratio = monthly_debt / monthly_income

        eligible = (
            monthly_income >= 8000 and
            debt_ratio <= 0.4 and
            credit_score >= 650
        )

        print("Ratio de deuda:", round(debt_ratio, 2))
        print("Elegible:", str(eligible).lower())

except ValueError:
    print("Error: entrada inválida")


"""
PROBLEMA 6: CALCULADORA DE IMC
Descripción: Calcular el IMC y mostrar sus banderas de categoría.
Entradas: weight_kg y height_m.
Salidas: IMC, Bajo peso, Normal y Sobrepeso.
Validaciones: El peso y la altura deben ser > 0.
Pruebas: Normal: 70, 1.75; Límite: 60, 2; Error: 0, 1.7.
"""

print("\nPROBLEMA 6: CALCULADORA DE IMC")

try:
    weight_kg = float(input("Ingresa el peso en kilogramos: "))
    height_m = float(input("Ingresa la altura en metros: "))

    if weight_kg <= 0 or height_m <= 0:
        print("Error: entrada inválida")

    if weight_kg > 0 and height_m > 0:
        bmi = weight_kg / (height_m * height_m)

        is_underweight = bmi < 18.5
        is_normal = bmi >= 18.5 and bmi < 25
        is_overweight = bmi >= 25

        print("IMC:", round(bmi, 2))
        print("Bajo peso:", str(is_underweight).lower())
        print("Normal:", str(is_normal).lower())
        print("Sobrepeso:", str(is_overweight).lower())


except ValueError:
    print("Error: entrada inválida")


# CONCLUSIONES
"""
int se usa para números enteros y float para números decimales.
Las comparaciones crean valores True o False.
if ayuda al programa a tomar decisiones.
and verifica si todas las condiciones son verdaderas.
or verifica si al menos una condición es verdadera.
La validación de entradas ayuda a prevenir cálculos incorrectos.
"""

# REFERENCIAS
"""
1. Documentación de Python. Tipos integrados.
https://docs.python.org/es/3/library/stdtypes.html

2. Documentación de Python. Tutorial de Python.
https://docs.python.org/es/3/tutorial/

3. Documentación de Python. Funciones incorporadas.
https://docs.python.org/es/3/library/functions.html

4. Documentación de Python. Introducción a Python.
https://docs.python.org/es/3/tutorial/introduction.html

5. Documentación de Python. Errores y excepciones.
https://docs.python.org/es/3/tutorial/errors.html
"""