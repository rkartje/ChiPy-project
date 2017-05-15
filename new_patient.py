class Patient:
    #init is a function that tacks some info onto an object
    #extend patient class to include diagnosis, medications, provider_id
    
    def __init__(self, name, birthdate, medical_number, phone_number, \
    diagnosis, medications, provider_id):
        self.name = name
        self.birthdate = birthdate
        self.medical_number = medical_number
        self.phone_number = phone_number
        self.diagnosis = diagnosis
        self.medications = medications
        self.provider_id = provider_id
        
        def record_encounter(self, date, reading):
        # to do
        pass

    #methods - mutators, to assign values to fields
    def set_name (self, name):
        self.__name = name #assigns value in name parameter to a Patient's object's __name field
        
    def set_birthdate (self, birthdate):
        self.__birthdate = birthdate
        
    def set_medical_number (self, medical_number):
        self.__medical_number = medical_number
        
    def set_phone_number (self, phone_number):
        self.__phone_number = phone_number
        
    def set_diagnosis (self, diagnosis):
        self.__diagnosis = diagnosis
        
    def set_medications (self, medications):
        self.__medications = medications
        
    def set._provider_id (self, provider_id):
        self.__provider_id = provider_id
        
    #methods - assessors, to get values from fields
    def get_name (self):
        return self.__name
        
    def get_birthdate (self):
        return self.__birthdate
        
    def get_medical_number (self):
        return self.__medical_number
        
    def get_phone_number (self):
        return self.__phone_number
        
    def get_diagnosis (self):
        return self.__diagnosis
        
    def get_medications (self):
        return self.__medications
        
    def get_provider_id (self):
        return self.__provider_id
        
