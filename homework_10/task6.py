def car_info(manufacturer, year=2024, **other_info):
    print(f"Manufacturer: {manufacturer}")
    print(f"Year: {year}")
    if other_info:
        print("other_info:")
        for info, value in other_info.items():
            print(f"  {info}: {value}")
    print()

car_info("Toyota")
car_info("mercedez", 2020, color="black", doors=4)
car_info("Tesla", autopilot=True, battery="100 kWh", range="350 miles")
car_info("BMW", 2021, model="X5", seats=5)