class Encounter:
    def __init__(self, patient, provider, timestamp, reading):
        self.patient = patient
        self.provider = provider
        self.timestamp = timestamp
        self.reading = reading
        
    #Mutators
    def set_patient (self, patient):
        self.__patient = patient #value in patient parameter assigned to Object's patient field
        
    def set_provider (self, provider):
        self__provider = provider
        
    def set_timestamp (self, timestamp):
        self__timestamp = timestamp
        
    def set_reading (self, reading):
        self__reading = reading
        
    #accessors
    def get_patient(self):
        return self.__patient
        
    def get_provider (self):
        return self.__provider
        
    def get_timestamp (self):
        return self-__timestamp
        
    def get_reading (self):
        return self.__reading
        
    
        
