# PYTHON STRINGS ASSIGNMENT
"""
Name: Jose Valentin Alvarez Reyes
Tuition: 2630144
Group: 3
"""

# EXECUTIVE SUMMARY
"""
A string is a sequence of characters.
Strings can be joined, compared, searched, and separated.
Strings are immutable, so methods create new strings.
strip() removes extra spaces.
lower() and upper() change capitalization.
split() separates text into a list.
This assignment contains six basic string exercises.
"""

# GOOD PRACTICES
"""
Use strip() to remove extra spaces.
Use lower() to compare text.
Use len() to count characters.
Use for to repeat an action for each item.
Use if to check a condition.
Strings cannot be changed directly.
"""

"""
PROBLEM 1: FULL NAME FORMATTER
Description: Format a name and display initials.
Inputs: full_name.
Outputs: formatted name and initials.
Validations: at least two words.
Tests: Normal: "jose valentin alvarez", Border: "roberto hernandez", Error: "   ".
"""

print("PROBLEM 1: FULL NAME FORMATTER")

full_name = input("Enter your full name: ")
full_name = full_name.strip()
name_parts = full_name.split()

if full_name == "":
    print("Error: name cannot be empty")

if full_name != "":
    if len(name_parts) < 2:
        print("Error: enter at least two words")

    if len(name_parts) >= 2:
        formatted_name = " ".join(name_parts).title()
        initials = ""

        for word in name_parts:
            initials = initials + word[0].upper() + "."

        print("Formatted name: " + formatted_name)
        print("Initials: " + initials)

"""
PROBLEM 2: EMAIL VALIDATOR
Description: Check a basic email format.
Inputs: email_text.
Outputs: validity and domain.
Validations: one @, a dot in the domain, no spaces.
Tests: Normal: "student@example.com", Border: "a@b.c", Error: "student example.com".
"""

print("\nPROBLEM 2: EMAIL VALIDATOR")

email_text = input("Enter an email: ")
email_text = email_text.strip()

if email_text == "":
    print("Error: email cannot be empty")

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
        print("Valid email: true")
        print("Domain: " + domain)

    if valid_email == False:
        print("Valid email: false")


"""
PROBLEM 3: PALINDROME CHECKER
Description: Check if a phrase reads the same backward.
Inputs: phrase.
Outputs: palindrome result.
Validations: at least three characters.
Tests: Normal: "Anita lava la tina", Border: "aba", Error: "   ".
"""

print("\nPROBLEM 3: PALINDROME CHECKER")

phrase = input("Enter a phrase: ")
phrase = phrase.strip()

if phrase == "":
    print("Error: phrase cannot be empty")

if phrase != "":
    clean_phrase = phrase.lower()
    clean_phrase = "".join(clean_phrase.split())

    if len(clean_phrase) < 3:
        print("Error: enter at least three characters")

    if len(clean_phrase) >= 3:
        reverse_phrase = clean_phrase[::-1]

        if clean_phrase == reverse_phrase:
            print("Is palindrome: true")

        if clean_phrase != reverse_phrase:
            print("Is palindrome: false")


"""
PROBLEM 4: SENTENCE WORD STATS
Description: Count words and find the first, last,
shortest, and longest words.
Inputs: sentence.
Outputs: word statistics.
Validations: sentence cannot be empty.
Tests: Normal: "Python makes coding fun", Border: "hello", Error: "   ".
"""

print("\nPROBLEM 4: SENTENCE WORD STATS")

sentence = input("Enter a sentence: ")
sentence = sentence.strip()

if sentence == "":
    print("Error: sentence cannot be empty")

if sentence != "":
    words = sentence.split()
    shortest_word = words[0]
    longest_word = words[0]

    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word

        if len(word) > len(longest_word):
            longest_word = word

    print("Word count: " + str(len(words)))
    print("First word: " + words[0])
    print("Last word: " + words[-1])
    print("Shortest word: " + shortest_word)
    print("Longest word: " + longest_word)


"""
PROBLEM 5: PASSWORD STRENGTH
Description: Classify a password as weak, medium,
or strong.
Inputs: password_input.
Outputs: password strength.
Rules:
Strong: 8+ characters, uppercase, lowercase,
digit, and symbol.
Medium: 8+ characters and at least two types.
Weak: does not meet the other rules.
Tests: Normal: "GoodPass8!", Border: "Abcdef12", Error: "".
"""

print("\nPROBLEM 5: PASSWORD STRENGTH")

password_input = input("Enter a password: ")

if password_input == "":
    print("Error: password cannot be empty")

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

    strength = "weak"

    if len(password_input) >= 8:
        if types_count >= 2:
            strength = "medium"

        if has_upper and has_lower and has_digit and has_symbol:
            strength = "strong"

    print("Password strength: " + strength)


"""
PROBLEM 6: PRODUCT LABEL
Description: Create a product label with 30 characters.
Inputs: product_name and price_text.
Outputs: label with exactly 30 characters.
Validations: name cannot be empty; price must be positive.
Tests: Normal: "Pen", "12.50"; Border: "A", "1"; Error: "Pen", "zero".
"""

print("\nPROBLEM 6: PRODUCT LABEL")

product_name = input("Enter a product name: ")
product_name = product_name.strip()
price_text = input("Enter a positive price: ")
price_text = price_text.strip()

if product_name == "":
    print("Error: product name cannot be empty")

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
        print("Error: price must be a positive number")

    if valid_price == True:
        price_display = "{:.2f}".format(price_value)

        label = "Product: " + product_name
        label = label + " | Price: $" + price_display

        if len(label) > 30:
            label = label[0:30]

        if len(label) < 30:
            spaces = 30 - len(label)
            label = label + (" " * spaces)

        print('Label: "' + label + '"')
        print("Label length: " + str(len(label)))



# CONCLUSIONS
"""
Strings help us process and display text.
strip() removes extra spaces.
lower() changes letters to lowercase.
split() separates text into words.
for repeats actions for each item.
if checks whether a condition is true.
Slicing extracts or reverses part of a string.
Validations help prevent incorrect input.
"""

# REFERENCES
"""
1. Python Documentation - Text Sequence Type: str
https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

2. Python Documentation - Built-in Functions
https://docs.python.org/3/library/functions.html

3. Python Tutorial - Introduction
https://docs.python.org/3/tutorial/introduction.html

4. Python Tutorial - Input and Output
https://docs.python.org/3/tutorial/inputoutput.html

5. Python Tutorial - Errors and Exceptions
https://docs.python.org/3/tutorial/errors.html
"""