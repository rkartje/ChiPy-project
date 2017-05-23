class Patient:
    #init is a function that tacks some info onto an object
    #extend patient class to include diagnosis, medications, provider_id
    #After further consideration will add 2 new variables and methods 
    #and consider removing the Encounter class.
    #Logical to keep BG data in Patient class.
    #Need to format fields??
    
    def __init__(self, name, birthdate, medical_number, phone_number, \
    diagnosis, medications, provider_id, reading=None, timestamp):
        self.name = name
        self.birthdate = birthdate 
        self.medical_number = medical_number
        self.phone_number = phone_number
        self.diagnosis = diagnosis
        self.medications = medications
        self.provider_id = provider_id
        self.readings = [] #append readings as they are done
        
        if reading is not None:
            self.readings.append(reading)
        
        self.timestamp = "" #append with dates and times as readings are
        #done. 
        
        if self.timestamp is not None:
            self.timestamp.append(timestamp)
        
    #add readings for this patient with the statement below. 
        
    def add_reading (self,reading):
        self.readings.append(reading)
        
    #add dates and times as readings are done with statement below.
        
    def add_timestamp (self, timestamp): #these need to correlate with the readings!How to do that??
        self.timestamp.append(timestamp)
        
#create an instance to this class, ie, create a new patient
patient1 = Patient ("Joseph Smith", "August 4, 1950", "12345-1",\
        "(708)345-8967", "type 2 diabetes mellitus", "metformin",\
        "DR1", 90, "22MAY170300")
        #having issues with date and time, shows 0!
        #cannot do add datetimestamp method, get an attribute error
        
#OUTPUT: bash: line 1: Updated Patient Class: command not found
#what does that mean?? Can run this on textbook IDLE.
# NS: This is due to the (previously) missing .py file extension.

        