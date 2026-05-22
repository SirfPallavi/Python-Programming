def insert_patient_data(name:str, age:int):
    if type(name) == str and type(age) ==int:
        print(name)
        print(age)
        print("data inserted successfully")
    else:
        raise TypeError("invalid data types")
    
    insert_patient_data("Pallavi",20)