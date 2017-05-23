class Encounter:
    #Encounter has a reference to a patient. 
    def __init__(self, reading, timestamp):
        self.reading = reading
        self.timestamp = timestamp
        
    def __repr__(self):
        return "Encounter(, {self.reading}, {self.timestamp})".format(self=self)
   
class Diagnosis:
    def __init__ (self, "diagnosis1", "diagnosis2", "diagnosis3")
    #how to add to a list when you don't know ahead of time how long list
    #will be? Here assume patients have 3 diagnoses.
        self.diagnosis1 = diagnosis1
        self.diagnosis2 = diagnosis2
        self.diagnosis3 = diagnosis3
        
class Medication:
    def __init__ (self, med1, med2, med3)
    #see comment for Diagnosis class
        self.med1 = med1
        self.med2 = med2
        self.med3 = med3

class Patient:
    #init is a function that tacks some info onto an object
    #extend patient class to include diagnosis, medications, provider_id, \
    #encounter=None
    
    
    def __init__(self, name, birthdate, medical_number, phone_number, \
    provider_id,medication=None, diagnosis=None, encounter=None):
        self.name = name
        self.birthdate = birthdate 
        self.medical_number = medical_number
        self.phone_number = phone_number
        self.medications = medications
        self.provider_id = provider_id
        self.encounters = []
        self.diagnosis = []
        self.medications = []
        
        #if there is an encounter add it to the list otherwise leave blank
        if encounter is not None:
            self.encounters.append(encounter)
            
        #if there is a diagnosis add it to the list otherwise leave blank
        #add a prompt for the user to enter data?
        if diagnosis is not None:
            self.diagnosis.append(diagnosis)
            
        #if there is a medication to add, add it otherwise leave blank.
        #add a prompt for the user to enter data?
        if medication is not None:
            self.medications.append(medication)
        
    #add encounters for a patient with the statement below. 
    #def add_encounter(self, encounter):
        #self.encounters.append(encounter)
        
#create an instance to this class, ie, create a new patient
#patient1 = Patient ("Joseph Smith", "August 4, 1950", "12345-1",\
#        "(708)345-8967", "type 2 diabetes mellitus", "metformin",\
#        "DR1", Encounter(90, "22-MAY-17-0300"))

#patient1 = Patient("Joe", Encounter(90, "May 22"))
#patient2 = Patient("Sharon")
#patient3 = Patient("Aarti")
#patient4 = Patient("Young")

#patient2.add_encounter(Encounter(75, "Apr 17"))
#patient4.add_encounter(Encounter(24, "May 19"))

       
        