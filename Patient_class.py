#class Encounter:
    #Encounter has a reference to a patient. 
    #def __init__(self, reading, timestamp):
        #self.reading = reading
        #self.timestamp = timestamp
        
    #def __repr__(self):
        #return "Encounter(, {self.reading}, {self.timestamp})".format(self=self)
   
class Diagnosis:
     def __init__(self, diagnosis=None):
     #if there is a diagnosis add it to the list otherwise leave blank
         self.diagnosis = []        
        
class Medication:
    def __init__(self, medication=None):
    #if there is a medication add it to the list otherwise leave blank.
        self.medication = []
        
class Provider:
    #provider id is a 3 digit number
    #provider name is first initial and last name
    def __init__ (self, provider_id, provider_name, provider_phone, provider_email, specialty=None):
        self.provider_id = provider_id
        self.provider_name = provider_name
        self.provider_phone = provider_phone
        self.provider_email = provider_email
        self.specialty = []
        
        
        #if provider is board certifed add that otherwise leave blank
        #this information is probably not necessary for this app
        #if board_certified is not None:
            #self.board_certified.append(board_certified)
            
    
        #if there is a specialty add it to the list otherwise leave blank
        #usually this is just one specialty so don't need a list?
        #does this need to be a list? Maybe it should be a Boolean?
        if specialty is not None:
            self.specialty.append(specialty)
        

#create an instance of this class
provider1 = Provider (345, "pshah", "(630) 986-1177", "pshah@umc.edu", "general_medicine")
print provider1.provider_name
print provider1.provider_phone

#create another instance of this class
provider2 = Provider(789, "jphillips", "(630)256-7000", "jphil@umc.edu", "endocrinology")        

class Patient:
    #init is a function that tacks some info onto an object
    #extend patient class to include diagnosis, medications, provider_id, \
    #encounter=None
    
    
    def __init__(self, name, birthdate, medical_number, phone_number, \
    provider_id, medication=None, diagnosis=None, encounter=None):
        self.name = name
        self.birthdate = birthdate 
        self.medical_number = medical_number
        self.phone_number = phone_number
        self.medication = medication
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
        
#create instances to this class, ie, create a new patient
patient1 = Patient ("joe", "August 4, 1950", "12345-1",\
        "(708)345-8967", "type 2 diabetes mellitus", "metformin",\
        "pshah", encounter(90, "22-MAY-17-0300"))
        
patient2 = Patient("sharon", "June 5, 1950", "56789-1", \
        "(815)272-5437", "type 2 diabetes mellitus", "glucotrol", \
        "jphillips", encounter(92, "30-MAY-17-1800"))

#how to add more encounters? 
#patient1 = Patient ("joe", Encounter (76, "30-MAY-17-1800"))
#patient2 = Patient("sharon")
#patient3 = Patient("Aarti")
#patient4 = Patient("Young")

#patient2.add_encounter(Encounter(75, "Apr 17"))
#patient4.add_encounter(Encounter(24, "May 19"))

def find_encounters_for(patient):
    return patient.encounters
    
joes_encounters = find_encounters_for(joe)
print joes_encounters





       
        