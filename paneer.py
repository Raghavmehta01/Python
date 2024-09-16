class Patient:
    def __init__(self,patient_id,patient_name):
        self.patient_id = patient_id
        self.patient_name = patient_name
        
        
class Doctor(Patient):
    def __init__(self,doc_name,ph):
        self.history = []
        self.ph = ph
        self.history.extend(self.ph)
        
        print(self.patient_id)
        print(self.patient_name)
        self.doc_name = doc_name
        
    def med(self,med_name):
        self.med_name = med_name
        input("Enter medicine name : ")
        
        
    def test(self,test_name):
        self.test_name = test_name
        
        
        
        
        
