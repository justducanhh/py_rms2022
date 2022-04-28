class Customer:
    def __init__ (self,)->None:
        self.__first = ""
        self.__last = ""
        self.__phone = ""
    
    def set_first (self , first):
        self._first = first
    def get_first (self , first):
        self._first = first
    
    def set_last (self , last):
        self._last = last
    def get_last (self , last):
        self._last = last
    
    def set_phone (self , phone):
        self._phone = phone 
    def get_phone (self , phone):
        self._phone = phone
    
    def get_full_name(self):
        return f"{self.__first} {self.__last}"
    
    
    def input_info (self):
        self.set_first(input("Enter customer first name :"))
        self.set_last(input("Enter customer last name : "))
        self.set_phone(input("Enter customer phone number : "))
        
    def _str_(self):
         return f"Phone number {self.get_phone()} is the phone number of customer name {self.get_full_name()} "
