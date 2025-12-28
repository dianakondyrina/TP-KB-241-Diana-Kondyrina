class Student :
    def __init__(self, name, phone, address, date):
        self.name = name
        self.phone = phone
        self.address = address
        self.date = date
    
    def __str__(self):
        return f"Information about {self.name}: {self.phone} | {self.address} | {self.date}"
    
    def to_dict (self) :
        return {
            "name": self.name,
            "phone": self.phone,
            "address": self.address,
            "date": self.date
        }
    