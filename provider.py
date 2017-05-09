Class Provider:
    def __init__ (self, prov_id, provider_lastname, provider_phone_number, provider_email):
        #think of better variable and field names
        self.prov_id = prov_id
        self.provider_lastname = provider_lastname
        self.provider_phone_number = provider_phone_number
        self.provider_email = provider_email
        
    #mutators
    def set_prov_id (self, prov_id):
        self.__prov_id = prov_id
        
    def set_provider_lastname (self, provider_lastname):
        self.__provider_lastname
        
    def set_provider_phone+number (self, provider_phone_number):
        self___provider_phone_number = provider_phone_number
        
    def set_provider_email (self, provider_email):
        self__provider_email = provider_email
        
    #accessors
    def get_prov_id (self):
        return self.__prov_id
        
    def get_provider_lastname (self):
        return self.__provider_lastname
        
    def get_provider_phone_number (self):
        return self.__provider_phone_number
        
    def get_provider_email (self):
        return self.__provider_email 
