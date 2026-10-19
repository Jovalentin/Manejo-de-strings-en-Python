# MANEJO DE STRINGS EN PYTHON
"""
Nombre: Jose Valentin Alvarez Reyes
Matrícula: 2630144
Grupo: 3
"""

# RESUMEN EJECUTIVO
"""
Una cadena es una secuencia de caracteres.
Las cadenas se pueden unir, comparar, buscar y separar.
Las cadenas son inmutables, por lo que los métodos crean nuevas cadenas.
strip() elimina espacios extra.
lower() y upper() cambian la capitalización.
split() separa el texto en una lista.
Esta asignación contiene seis ejercicios básicos de cadenas.
"""

# BUENAS PRÁCTICAS
"""
Usar strip() para eliminar espacios extra.
Usar lower() para comparar texto.
Usar len() para contar caracteres.
Usar for para repetir una acción por cada elemento.
Usar if para verificar una condición.
Las cadenas no se pueden modificar directamente.
"""

"""
PROBLEMA 1: FORMATEADOR DE NOMBRE COMPLETO
Descripción: Formatear un nombre y mostrar las iniciales.
Entradas: full_name.
Salidas: nombre formateado e iniciales.
Validaciones: al menos dos palabras.
Pruebas: Normal: "jose valentin alvarez", Límite: "roberto hernandez", Error: "   ".
"""

print("PROBLEMA 1: FORMATEADOR DE NOMBRE COMPLETO")

full_name = input("Ingresa tu nombre completo: ")
full_name = full_name.strip()
name_parts = full_name.split()

if full_name == "":
    print("Error: el nombre no puede estar vacío")

if full_name != "":
    if len(name_parts) < 2:
        print("Error: ingresa al menos dos palabras")

    if len(name_parts) >= 2:
        formatted_name = " ".join(name_parts).title()
        initials = ""

        for word in name_parts:
            initials = initials + word[0].upper() + "."

        print("Nombre formateado: " + formatted_name)
        print("Iniciales: " + initials)

"""
PROBLEMA 2: VALIDADOR DE CORREO ELECTRÓNICO
Descripción: Verificar un formato básico de correo electrónico.
Entradas: email_text.
Salidas: validez y dominio.
Validaciones: un @, un punto en el dominio, sin espacios.
Pruebas: Normal: "student@example.com", Límite: "a@b.c", Error: "student example.com".
"""

print("\nPROBLEMA 2: VALIDADOR DE CORREO ELECTRÓNICO")

email_text = input("Ingresa un correo electrónico: ")
email_text = email_text.strip()

if email_text == "":
    print("Error: el correo no puede estar vacío")

if email_text != "":
    valid_email = True

    if email_text.count("@") != 1:
        valid_email = False

    if " " in email_text:
        valid_email = False

    if email_text.count("@") == 1:
        at_position = email_text.find("@")
        domain = email_text[at_position + 1:]

        if at_position == 0:
            valid_email = False

        if "." not in domain:
            valid_email = False

        if domain == "":
            valid_email = False

        if domain.startswith("."):
            valid_email = False

        if domain.endswith("."):
            valid_email = False

    if valid_email == True:
        print("Correo válido: verdadero")
        print("Dominio: " + domain)

    if valid_email == False:
        print("Correo válido: falso")


"""
PROBLEMA 3: VERIFICADOR DE PALÍNDROMOS
Descripción: Verificar si una frase se lee igual al derecho y al revés.
Entradas: phrase.
Salidas: resultado de palíndromo.
Validaciones: al menos tres caracteres.
Pruebas: Normal: "Anita lava la tina", Límite: "aba", Error: "   ".
"""

print("\nPROBLEMA 3: VERIFICADOR DE PALÍNDROMOS")

phrase = input("Ingresa una frase: ")
phrase = phrase.strip()

if phrase == "":
    print("Error: la frase no puede estar vacía")

if phrase != "":
    clean_phrase = phrase.lower()
    clean_phrase = "".join(clean_phrase.split())

    if len(clean_phrase) < 3:
        print("Error: ingresa al menos tres caracteres")

    if len(clean_phrase) >= 3:
        reverse_phrase = clean_phrase[::-1]

        if clean_phrase == reverse_phrase:
            print("Es palíndromo: verdadero")

        if clean_phrase != reverse_phrase:
            print("Es palíndromo: falso")


"""
PROBLEMA 4: ESTADÍSTICAS DE PALABRAS EN UNA ORACIÓN
Descripción: Contar palabras y encontrar la primera, última,
más corta y más larga.
Entradas: sentence.
Salidas: estadísticas de palabras.
Validaciones: la oración no puede estar vacía.
Pruebas: Normal: "Python makes coding fun", Límite: "hello", Error: "   ".
"""

print("\nPROBLEMA 4: ESTADÍSTICAS DE PALABRAS EN UNA ORACIÓN")

sentence = input("Ingresa una oración: ")
sentence = sentence.strip()

if sentence == "":
    print("Error: la oración no puede estar vacía")

if sentence != "":
    words = sentence.split()
    shortest_word = words[0]
    longest_word = words[0]

    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word

        if len(word) > len(longest_word):
            longest_word = word

    print("Cantidad de palabras: " + str(len(words)))
    print("Primera palabra: " + words[0])
    print("Última palabra: " + words[-1])
    print("Palabra más corta: " + shortest_word)
    print("Palabra más larga: " + longest_word)


"""
PROBLEMA 5: FUERZA DE LA CONTRASEÑA
Descripción: Clasificar una contraseña como débil, media
o fuerte.
Entradas: password_input.
Salidas: fuerza de la contraseña.
Reglas:
Fuerte: 8+ caracteres, mayúscula, minúscula,
dígito y símbolo.
Media: 8+ caracteres y al menos dos tipos.
Débil: no cumple las otras reglas.
Pruebas: Normal: "GoodPass8!", Límite: "Abcdef12", Error: "".
"""

print("\nPROBLEMA 5: FUERZA DE LA CONTRASEÑA")

password_input = input("Ingresa una contraseña: ")

if password_input == "":
    print("Error: la contraseña no puede estar vacía")

if password_input != "":
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for character in password_input:
        if character.isupper():
            has_upper = True

        if character.islower():
            has_lower = True

        if character.isdigit():
            has_digit = True

        if not character.isalnum():
            has_symbol = True

    types_count = 0

    if has_upper == True:
        types_count = types_count + 1

    if has_lower == True:
        types_count = types_count + 1

    if has_digit == True:
        types_count = types_count + 1

    if has_symbol == True:
        types_count = types_count + 1

    strength = "débil"

    if len(password_input) >= 8:
        if types_count >= 2:
            strength = "media"

        if has_upper and has_lower and has_digit and has_symbol:
            strength = "fuerte"

    print("Fuerza de la contraseña: " + strength)


"""
PROBLEMA 6: ETIQUETA DE PRODUCTO
Descripción: Crear una etiqueta de producto con 30 caracteres.
Entradas: product_name y price_text.
Salidas: etiqueta con exactamente 30 caracteres.
Validaciones: el nombre no puede estar vacío; el precio debe ser positivo.
Pruebas: Normal: "Pen", "12.50"; Límite: "A", "1"; Error: "Pen", "zero".
"""

print("\nPROBLEMA 6: ETIQUETA DE PRODUCTO")

product_name = input("Ingresa el nombre del producto: ")
product_name = product_name.strip()
price_text = input("Ingresa un precio positivo: ")
price_text = price_text.strip()

if product_name == "":
    print("Error: el nombre del producto no puede estar vacío")

if product_name != "":
    price_check = price_text.replace(".", "")
    valid_price = True

    if price_text == "":
        valid_price = False

    if price_check.isdigit() == False:
        valid_price = False

    if price_text.count(".") > 1:
        valid_price = False

    if price_text.count(".") == 1:
        price_parts = price_text.split(".")

        if price_parts[0] == "":
            valid_price = False

        if price_parts[1] == "":
            valid_price = False

    if valid_price == True:
        price_value = float(price_text)

        if price_value <= 0:
            valid_price = False

    if valid_price == False:
        print("Error: el precio debe ser un número positivo")

    if valid_price == True:
        price_display = "{:.2f}".format(price_value)

        label = "Producto: " + product_name
        label = label + " | Precio: $" + price_display

        if len(label) > 30:
            label = label[0:30]

        if len(label) < 30:
            spaces = 30 - len(label)
            label = label + (" " * spaces)

        print('Etiqueta: "' + label + '"')
        print("Longitud de la etiqueta: " + str(len(label)))



# CONCLUSIONES
"""
Las cadenas nos ayudan a procesar y mostrar texto.
strip() elimina espacios extra.
lower() cambia las letras a minúsculas.
split() separa el texto en palabras.
for repite acciones por cada elemento.
if verifica si una condición es verdadera.
El slicing extrae o invierte parte de una cadena.
Las validaciones ayudan a prevenir entradas incorrectas.
"""

# REFERENCIAS
"""
1. Documentación de Python - Tipo de secuencia de texto: str
https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

2. Documentación de Python - Funciones integradas
https://docs.python.org/3/library/functions.html

3. Tutorial de Python - Introducción
https://docs.python.org/3/tutorial/introduction.html

4. Tutorial de Python - Entrada y salida
https://docs.python.org/3/tutorial/inputoutput.html

5. Tutorial de Python - Errores y excepciones
https://docs.python.org/3/tutorial/errors.html
"""