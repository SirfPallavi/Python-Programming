import re

# Regex patterns
name_pattern = r'^[A-Za-z ]{3,30}$'
address_pattern = r'^[A-Za-z0-9\s,.\-\/]{10,100}$'
student_id_pattern = r'^STU\d{4}$'
password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$'

# -------- REGISTRATION --------
print("----- Registration -----")

name = input("Enter Name: ")
if not re.match(name_pattern, name):
    print("Invalid Name")
    exit()

address = input("Enter Address: ")
if not re.match(address_pattern, address):
    print("Invalid Address")
    exit()

student_id = input("Enter Student ID: ")
if not re.match(student_id_pattern, student_id):
    print("Invalid Student ID (Format: STU1234)")
    exit()

password = input("Enter Password: ")
if not re.match(password_pattern, password):
    print("Invalid Password")
    exit()

print("Registration successful")

# -------- LOGIN --------
print("\n----- Login -----")

login_id = input("Enter Student ID: ")
login_password = input("Enter Password: ")

if login_id == student_id and login_password == password:
    print("Login successful")
else:
    print("Invalid student ID or password")
