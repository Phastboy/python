#car_price() function
def car_price(price, years):
    #checking number of years
    if years==0:
        return round(price, 2)
    else:
        value_lost=price*0.2
        #value after depreciation
        new_price=round(price-value_lost, 2)
        return car_price(new_price, years-1)

price=float(input("enter the amount the car was purchased(#): "))
years=float(input("how many years has it been used: "))
car_value=car_price(price, years)
print(f"the car's worth after {years} years is #{car_value}")