class Encounter:
    def __init__(self, reading, timestamp):
        self.reading = reading
        self.timestamp = timestamp
    
    def __repr__(self):
        return "Encounter(, {self.reading}, {self.timestamp})".format(self=self)


class Patient:
    #init is a function that tacks some info onto an object
    #extend patient class to include diagnosis, medications, provider_id
    #After further consideration will add 2 new variables and methods 
    #and consider removing the Encounter class.
    #Logical to keep BG data in Patient class.
    #Need to format fields??
    
    def __init__(self, name, birthdate, medical_number, phone_number, \
    diagnosis, medications, provider_id, encounter=None):
        self.name = name
        self.birthdate = birthdate 
        self.medical_number = medical_number
        self.phone_number = phone_number
        self.diagnosis = diagnosis
        self.medications = medications
        self.provider_id = provider_id
        self.encounters = []
        
        if encounter is not None:
            self.encounters.append(encounter)
        
    #add readings for this patient with the statement below. 
        
    def add_encounter(self, encounter):
        self.encounters.append(encounter)
        
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

        #having issues with date and time, shows 0!
        #cannot do add datetimestamp method, get an attribute error
        
#OUTPUT: bash: line 1: Updated Patient Class: command not found
#what does that mean?? Can run this on textbook IDLE.
# NS: This is due to the (previously) missing .py file extension.

        