# Learning intentions:
# - Create a class pet with same information as in previous examples
# - Create an object instance of class pet

class Pet:
    def __init__(self, name, category, age, vaccination_status):
        self.name = name
        self.category = category
        self.age = age
        self.vaccination_status = vaccination_status
        self.cc = "unknown"
        self.billing_address = "unknown"
        self.owner_name = "unknown"
        self.account_balance - "unknown"


p1 = Pet("Monkey", "Cat", 6, "Vacccinated", "4434 000 000 000", "Melissa Topp", 125.50, "24 Kalang Avenue, St Marys")
p2 = Pet("Fred", "Dog", 11, "Vacccinated", "4434 000 000 000", "Melissa Topp", 125.50, "24 Kalang Avenue, St Marys")



#ACTIVITIES:
#1. Print out vaccination status of Bonnie
#2. Create another pet named Foxy who is a dog
#3. Add the following attributes to the pet class:
# - credit card
# - billing address
# - owner name (preset to unknown)
# - account balance (pre set to 0)