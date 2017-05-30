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
        if board_certified is not None:
            self.board_certified.append(board_certified)
            
    
        #if there is a specialty add it to the list otherwise leave blank
        #usually this is just one specialty so don't need a list?
        #does this need to be a list? Maybe it should be a Boolean?
        if specialty is not None:
            self.specialty.append(specialty)
        

#create an instance of this class
provider1 = Provider (345, "pshah", "(630) 986-1177", "pshah@umc.edu", "general_medicine", "board_certified")
print provider1.provider_name
print provider1.provider_phone

#create another instance of this class
provider2 = Provider(789, "jphillips", "(630)256-7000", "jphil@umc.edu", "endocrinology")
print provider2.provider_id, provider2.provider_name


print (provider2.specialty)

    
    