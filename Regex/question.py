import re
import os

# -------- CUSTOM EXCEPTION --------
class ValidationError(Exception):
    pass


# -------- STUDENT CLASS --------
class Student:

    FILE_NAME = "students.txt"

    # -------- VALIDATION METHODS --------

    def validate_name(self, name):
        if not re.match(r'^[A-Za-z ]{3,30}$', name):
            raise ValidationError("Name must be 3-30 characters (letters and spaces only)")
        return name

    def validate_address(self, address):
        if not re.match(r'^[A-Za-z0-9\s,.\-\/]{10,100}$', address):
            raise ValidationError("Invalid address format")
        return address

    def validate_student_id(self, student_id):
        if not re.match(r'^STU\d{4}$', student_id):
            raise ValidationError("Student ID must be like STU1234")
        return student_id

    def validate_password(self, password):
        if not re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$', password):
            raise ValidationError("Weak password")
        return password

    # -------- CHECK IF USER EXISTS --------

    def user_exists(self, student_id):
        if not os.path.exists(self.FILE_NAME):
            return False

        with open(self.FILE_NAME, "r") as file:
            for line in file:
                stored_id, _ = line.strip().split(",")
                if stored_id == student_id:
                    return True
        return False

    # -------- REGISTRATION --------

    def register(self):
        print("----- Registration -----")

        try:
            name = self.validate_name(input("Enter Name: "))
            address = self.validate_address(input("Enter Address: "))
            student_id = self.validate_student_id(input("Enter Student ID: "))

            if self.user_exists(student_id):
                raise ValidationError("Student ID already exists")

            password = self.validate_password(input("Enter Password: "))

            # Save to file
            with open(self.FILE_NAME, "a") as file:
                file.write(f"{student_id},{password}\n")

            print("Registration successful")
            return True

        except ValidationError as e:
            print(f"Error: {e}")
            return False

        except Exception as e:
            print(f"Unexpected error: {e}")
            return False

    # -------- LOGIN --------

    def login(self):
        print("\n----- Login -----")

        try:
            student_id = input("Enter Student ID: ")
            password = input("Enter Password: ")

            if not os.path.exists(self.FILE_NAME):
                raise ValidationError("No users registered yet")

            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    stored_id, stored_pass = line.strip().split(",")

                    if student_id == stored_id and password == stored_pass:
                        print("Login successful")
                        return

            raise ValidationError("Invalid student ID or password")

        except ValidationError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")


# -------- MAIN --------

student = Student()

choice = input("Enter 1 for Register, 2 for Login: ")

if choice == "1":
    student.register()
elif choice == "2":
    student.login()
else:
    print("Invalid choice")
