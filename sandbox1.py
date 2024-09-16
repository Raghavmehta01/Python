class Patient_records:
    def __init__(self, patient_id, patient_name, patient_cont):
        self.__patient_id = patient_id
        self.__patient_name = patient_name
        self.__patient_cont = patient_cont
        
  
    def get_id(self):
        return self.__patient_id
    
    def get_name(self):
        return self.__patient_name
    
    def get_cont(self):
        return self.__patient_cont
    
   
    def set_id(self, patient_id):
        self.__patient_id = patient_id
    
    def set_name(self, patient_name):
        self.__patient_name = patient_name
    
    def set_cont(self, patient_cont):
        self.__patient_cont = patient_cont

    
    
    def update_record(self):
        self.set_id(input("Enter patient ID: "))
        self.set_name(input("Enter patient name: "))
        self.set_cont(input("Enter patient contact number (format XXX-XXXX): "))

def display_menu():
    print("\nMenu:")
    print("1. View Patient Record")
    print("2. Update Patient Record")
    print("3. Exit")


patient_id = input("Enter patient ID: ")
name = input("Enter patient name: ")
contact_number = input("Enter patient contact: ")
patient = Patient_records(patient_id, name, contact_number)


while True:
    display_menu()
    choice = input("Enter your choice (1/2/3): ")
    
    match choice:
        case "1":
            
            print(f"Patient ID: {patient.get_id()}")
            print(f"Patient Name: {patient.get_name()}")
            print(f"Patient Contact Number: {patient.get_cont()}")
        case "2":
            
            patient.update_record()
        case "3":
            
            print("Exiting")
            break
        case _:
            
            print("Invalid choice")
