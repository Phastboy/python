#class Scooter with company name, starting fee, price per 100 meters and available distance as attribute 
class Scooter:
    def __init__(self, company_name, starting_fee, price_per_100m, available_distance):
        self.company_name = company_name
        self.starting_fee = starting_fee
        self.price_per_100m = price_per_100m
        self.available_distance = available_distance
#price() method with argument length
    def price(self, length):
        if length <= self.available_distance:
            return self.starting_fee + (length / 100) * self.price_per_100m
        else:
            return 1000
#ride() method with argument length 
    def ride(self, length):
        if length <= self.available_distance:
          self.available_distance -= length
        else:
          self.available_distance = 0
#charge() method with argument kilometers 
    def charge(self, kilometers):
        self.available_distance += kilometers

#class Rental with scooters attribute 
class Rental:
    def __init__(self, scooters):
        self.scooters = scooters
#distance() method with argument length 
    def display_choices(self, length):
        sorted_scooters = sorted(self.scooters, key=lambda scooter: scooter.price(length))
        for scooter in sorted_scooters:
            price = scooter.price(length)
            print(f"Scooter: {scooter.company_name}, Price: {price}")
#rent() method with arguments scooter name and length 
    def rent(self, scooter_name, length):
        for scooter in self.scooters:
            if scooter.company_name == scooter_name:
                if length <= scooter.available_distance:
                    price = scooter.price(length)
                    print(f"Renting {scooter_name}, Price: {price}")
                    scooter.ride(length)
                else:
                    print("You want to go to heaven?")
#charge_scooter() method with arguments scooter_name and kilometers
    def charge_scooter(self, scooter_name, kilometers):
        for scooter in self.scooters:
            if scooter.company_name == scooter_name:
                scooter.charge(kilometers)
                break


# Prompt the user for scooter details and create scooter objects
scooters = []
scooter_data = [
    ("Bolt", 1.5, 0.1, 20),
    ("Tuul", 1, 0.15, 18),
    ("Bird", 0, 0.3, 34)
]
#adding scooter details to scooters list
for data in scooter_data:
    company_name, starting_fee, price_per_100m, available_distance = data
    scooter = Scooter(company_name, starting_fee, price_per_100m, available_distance)
    scooters.append(scooter)

# Create an instance of the Rental class with the scooter objects
rental = Rental(scooters)

# Call the required methods on the rental instance
rental.display_choices(5)
rental.rent("Bolt", 3)
rental.rent("Tuul", 10)
rental.rent("Bird", 25)
rental.charge_scooter("Tuul", 5)
rental.rent("Tuul", 2)