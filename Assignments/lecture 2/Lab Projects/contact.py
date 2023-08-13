class Contact:
    def __init__(self):
        self.contacts = {}
        self.name=" "
        self.phone =""
            
        
    def add(self):
        self.name = input("Name:")
        self.phone = input("Number:")
        self.contacts[self.name] = self.phone
    
    
    def search(self):
        name1 = input("Name:")
        search = " "
        if len(self.contacts)<1 :
            print("You dont have any contact")
            return     
        for name,number in self.contacts.items() :
            if name == name1 :  
                search = (f"Name : {name} - Number : {number}")
                return search
        print("Not found")
        return False
    
    
    
    def print(self):
        for name , number in self.contacts.items():
            print (f"Name : {name} - Number : {number}")
    
    def remove(self):
        name1 = input("Name:")
        if len(self.contacts)<1 :
            print("You dont have any contact")
            return  
        #if self.contacts[name1] == self.contacts[name1]:
        for name in self.contacts :
            if name == name1 :
                self.contacts.pop(name1)
                break
                
                print("Deleted successfully")
        print("Not found")
        
        return False






contact = Contact()
while True:
    choice =  input("Enter # to stop\n1-Add contact\n2-Search contact\n3-Print contacts \n4-Delete contact\n5-Exit\nEnter:")
    if choice == "#":
        break
    if choice == "1":
        contact.add()
        
    elif choice == "2":
        print(contact.search())
        
    elif choice == "3":
        print(contact.print())
        
    elif choice == "4":
        print(contact.remove())
        
    elif choice == "5":
        break
    
    else :
        print("Error try again")